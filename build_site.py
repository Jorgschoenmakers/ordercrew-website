"""Build only the reviewed public files with Python standard-library tools."""
import base64
import hashlib
import json
from pathlib import Path, PurePosixPath
import sys

HERE = Path(__file__).resolve().parent
OUTPUT = HERE / 'ordercrew-site'
# Generated from the reviewed public source. Paths, encodings, sizes and hashes
# are independently fixed here as well as in site-source.json.
ALLOWED = {'apple-touch-icon.png': {'bytes': 11795,
                          'encoding': 'base64',
                          'sha256': 'ea199f80e75335a561a9c086995d4114527db3805d6cbbbfaddfaf3ed1da73fd'},
 'assets/auth.css': {'bytes': 9369,
                     'encoding': 'utf-8',
                     'sha256': '0173ddc138271c102ea74b1f27ddb3c2de405931abf535a4d003822b0273009b'},
 'assets/brand.svg': {'bytes': 1887,
                      'encoding': 'utf-8',
                      'sha256': '26e8d0aef8ca612a63d5bf1e540cbf6382d44823bb87d01fe7414318d4c6975f'},
 'assets/demo-access.js': {'bytes': 1634,
                           'encoding': 'utf-8',
                           'sha256': 'd3440d6ef511aaef8f699c2afb0156c2e6509409e25cb9d3353092ce4acc458a'},
 'assets/icons.svg': {'bytes': 12455,
                      'encoding': 'utf-8',
                      'sha256': 'df60d367bf536a7b2a8d8d1bf64d961c01e58267b684767af9ddff65b0be8a44'},
 'assets/login.js': {'bytes': 1662,
                     'encoding': 'utf-8',
                     'sha256': '10895f3dd7fe25c697147faa59749e3ab9ae1c8c81ecd49cb5531bbfc52ba56f'},
 'assets/site.css': {'bytes': 21674,
                     'encoding': 'utf-8',
                     'sha256': '86accb1cff9565a0e82339b1aeb7a33718984a9c87f4085a0b7ee0f1d2115207'},
 'assets/site.js': {'bytes': 8426,
                    'encoding': 'utf-8',
                    'sha256': 'df45ab5219720281f26dbd30c32d14d503b6147d3520f153238f9cc61a5588eb'},
 'demo.html': {'bytes': 216882,
               'encoding': 'utf-8',
               'sha256': 'b2216380f6e0aca778ba35241eff9e1bc4a50a2ba91c76ec9fe8723b74824a12'},
 'favicon-48.png': {'bytes': 2867,
                    'encoding': 'base64',
                    'sha256': 'eac6d5b71951b202b1d05fa3a2c2403361276ba995ad784dc1f017df1875d58e'},
 'favicon-96.png': {'bytes': 5969,
                    'encoding': 'base64',
                    'sha256': '55440026825f1fb7b043cc7be90188131269fe9eb5e8da891c26602214ce556c'},
 'favicon.ico': {'bytes': 5427,
                 'encoding': 'base64',
                 'sha256': 'e0b71a503e3387a944f9de67104242776c0a80258de72f13a6144331286d81da'},
 'favicon.svg': {'bytes': 1887,
                 'encoding': 'utf-8',
                 'sha256': '26e8d0aef8ca612a63d5bf1e540cbf6382d44823bb87d01fe7414318d4c6975f'},
 'icon-192.png': {'bytes': 11432,
                  'encoding': 'base64',
                  'sha256': 'db3619d8f2b6d1b9010627254fffad42916ab6f8dc7c544b0ff420bab7c26866'},
 'icon-512.png': {'bytes': 32929,
                  'encoding': 'base64',
                  'sha256': '1a4b38ce0074c71754f29abfb5525494c3d9a5700bb7b69e8ace829685b08ef2'},
 'index.html': {'bytes': 16039,
                'encoding': 'utf-8',
                'sha256': '6502c08f90948b3f6dd12974d5ccc8d685f7b69cedcfd11f90ae976deca40f11'},
 'login.html': {'bytes': 5725,
                'encoding': 'utf-8',
                'sha256': '33837518639f800ab9e69e4fa605456293cd9bb9b8c7569d5ae8412fd57f475b'},
 'privacy.html': {'bytes': 6006,
                  'encoding': 'utf-8',
                  'sha256': '5c7051ae9f86ec65f668aada3c98e27855137f5c6e27bbeebe349d06d9ee0fd9'},
 'robots.txt': {'bytes': 70,
                'encoding': 'utf-8',
                'sha256': '85a0d28ee26c036fae7c4bd4f1fc9afd7ff0d0e46f00d9827343334ef44be6cb'},
 'site.webmanifest': {'bytes': 581,
                      'encoding': 'utf-8',
                      'sha256': '1124818aa8af8b7aaefd1254b544a3e65c900d98f4d54513124f59eb4f33d3eb'},
 'sitemap.xml': {'bytes': 189,
                 'encoding': 'utf-8',
                 'sha256': 'e2867c4d88fb9e70a4255898decc9dc78dd33061c8085630cec478a36314441e'}}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def target_for(relative):
    path = PurePosixPath(relative)
    require(relative in ALLOWED, 'Path is not on the public allowlist: ' + relative)
    require(not path.is_absolute() and '..' not in path.parts and '\\' not in relative
            and ':' not in relative and path.as_posix() == relative, 'Unsafe output path')
    require(not OUTPUT.is_symlink() and OUTPUT.resolve() == OUTPUT,
            'Output directory may not redirect to another location')
    target = OUTPUT.joinpath(*path.parts)
    cursor = target
    while cursor != OUTPUT:
        require(not cursor.is_symlink(), 'Output path contains a symlink: ' + relative)
        cursor = cursor.parent
    require(target.resolve().is_relative_to(OUTPUT.resolve()), 'Output escapes the build directory')
    return target


def validated_files():
    source = json.loads((HERE / 'site-source.json').read_text(encoding='utf-8'))
    require(source.get('format_version') == 1, 'Unsupported source format')
    require(source.get('publish_directory') == 'ordercrew-site', 'Unexpected publish directory')
    entries = source.get('files')
    require(isinstance(entries, list) and len(entries) == len(ALLOWED), 'Unexpected public file count')
    prepared, seen = [], set()
    for entry in entries:
        require(isinstance(entry, dict), 'Invalid source entry')
        relative = entry.get('path')
        require(isinstance(relative, str), 'Missing source path')
        target = target_for(relative)
        require(relative not in seen, 'Duplicate public file: ' + relative)
        seen.add(relative)
        expected = ALLOWED[relative]
        require(all(entry.get(key) == expected[key] for key in ('encoding', 'bytes', 'sha256')),
                'Source metadata differs from the reviewed allowlist: ' + relative)
        chunks = entry.get('content')
        require(isinstance(chunks, list) and all(isinstance(item, str) for item in chunks),
                'Content must be an array of text lines: ' + relative)
        text = ''.join(chunks)
        data = text.encode('utf-8') if expected['encoding'] == 'utf-8' else base64.b64decode(text, validate=True)
        require(len(data) == expected['bytes'], 'Byte count mismatch: ' + relative)
        require(hashlib.sha256(data).hexdigest() == expected['sha256'], 'SHA256 mismatch: ' + relative)
        prepared.append((target, data, expected['sha256']))
    require(seen == set(ALLOWED), 'Missing or unexpected public file')
    if OUTPUT.exists():
        require(OUTPUT.is_dir(), 'Output is not a directory')
        for existing in OUTPUT.rglob('*'):
            require(not existing.is_symlink() and existing.resolve().is_relative_to(OUTPUT),
                    'Existing output contains a redirecting path')
            if existing.is_file():
                require(existing.relative_to(OUTPUT).as_posix() in ALLOWED,
                        'Unexpected existing public file; use a clean build directory')
    return prepared


def main():
    prepared = validated_files()
    OUTPUT.mkdir(exist_ok=True)
    for target, data, expected in prepared:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        require(hashlib.sha256(target.read_bytes()).hexdigest() == expected,
                'Written file failed verification: ' + target.name)
    print('OrderCrew build verified: ' + str(len(prepared)) + ' public files in ordercrew-site/.')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, TypeError, KeyError) as error:
        print('OrderCrew build failed: ' + str(error), file=sys.stderr)
        sys.exit(1)
