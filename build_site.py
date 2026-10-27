"""Build the reviewed public OrderCrew files using only Python's standard library.

Input: site-source.json beside this script.
Output: ordercrew-site/ beside this script, and no files anywhere else.
All source entries are validated before the output directory is created.
"""
import base64
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys

HERE = Path(__file__).resolve().parent
OUTPUT = HERE / 'ordercrew-site'
ALLOWED = {
    'apple-touch-icon.png': 'base64',
    'assets/auth.css': 'utf-8',
    'assets/brand.svg': 'utf-8',
    'assets/demo-access.js': 'utf-8',
    'assets/login.js': 'utf-8',
    'assets/site.css': 'utf-8',
    'assets/site.js': 'utf-8',
    'demo.html': 'utf-8',
    'favicon-48.png': 'base64',
    'favicon-96.png': 'base64',
    'favicon.ico': 'base64',
    'favicon.svg': 'utf-8',
    'icon-192.png': 'base64',
    'icon-512.png': 'base64',
    'index.html': 'utf-8',
    'login.html': 'utf-8',
    'privacy.html': 'utf-8',
    'robots.txt': 'utf-8',
    'site.webmanifest': 'utf-8',
    'sitemap.xml': 'utf-8',
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def safe_target(relative):
    path = PurePosixPath(relative)
    require(relative in ALLOWED, 'Path is not on the public-file allowlist: ' + relative)
    require(not path.is_absolute() and '..' not in path.parts and '\\' not in relative
            and ':' not in relative and path.as_posix() == relative, 'Unsafe output path')
    target = OUTPUT.joinpath(*path.parts)
    require(not OUTPUT.is_symlink(), 'Output directory may not be a symlink')
    require(OUTPUT.resolve() == OUTPUT, 'Output directory may not redirect to another location')
    cursor = target
    while cursor != OUTPUT:
        require(not cursor.is_symlink(), 'Output path may not contain symlinks: ' + relative)
        cursor = cursor.parent
    require(target.resolve().is_relative_to(OUTPUT.resolve()), 'Output path escapes the build directory')
    return target


def validated_files():
    source = json.loads((HERE / 'site-source.json').read_text(encoding='utf-8'))
    require(source.get('format_version') == 1, 'Unsupported source format')
    require(source.get('publish_directory') == 'ordercrew-site', 'Unexpected publish directory')
    entries = source.get('files')
    require(isinstance(entries, list) and len(entries) == len(ALLOWED), 'Expected exactly 20 public files')
    prepared, seen = [], set()
    for entry in entries:
        relative = entry.get('path')
        require(isinstance(relative, str), 'Missing file path')
        target = safe_target(relative)
        require(relative not in seen, 'Duplicate public file: ' + relative)
        seen.add(relative)
        require(entry.get('encoding') == ALLOWED[relative], 'Unexpected encoding: ' + relative)
        chunks = entry.get('content')
        require(isinstance(chunks, list) and all(isinstance(item, str) for item in chunks),
                'Content must be an array of text lines: ' + relative)
        text = ''.join(chunks)
        data = text.encode('utf-8') if entry['encoding'] == 'utf-8' else base64.b64decode(text, validate=True)
        require(type(entry.get('bytes')) is int and len(data) == entry['bytes'], 'Byte count mismatch: ' + relative)
        expected = entry.get('sha256', '')
        require(isinstance(expected, str) and re.fullmatch(r'[0-9a-f]{64}', expected), 'Invalid SHA256: ' + relative)
        require(hashlib.sha256(data).hexdigest() == expected, 'SHA256 mismatch: ' + relative)
        prepared.append((relative, target, data, expected))
    require(seen == set(ALLOWED), 'Missing or unexpected public file')
    if OUTPUT.exists():
        require(OUTPUT.is_dir(), 'Output exists and is not a directory')
        for existing in OUTPUT.rglob('*'):
            require(not existing.is_symlink(), 'Existing output contains a symlink')
            if existing.is_file():
                require(existing.relative_to(OUTPUT).as_posix() in ALLOWED,
                        'Output contains an unexpected file; use a clean build directory')
    return prepared


def main():
    prepared = validated_files()
    OUTPUT.mkdir(exist_ok=True)
    for relative, target, data, expected in prepared:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        require(hashlib.sha256(target.read_bytes()).hexdigest() == expected,
                'Written file failed verification: ' + relative)
    print('OrderCrew build verified: 20 public files written to ordercrew-site/.')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, TypeError, KeyError) as error:
        print('OrderCrew build failed: ' + str(error), file=sys.stderr)
        sys.exit(1)
