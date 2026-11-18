"""Build only the reviewed public files with Python standard-library tools."""
import base64
import hashlib
import json
from pathlib import Path, PurePosixPath
import sys

HERE = Path(__file__).resolve().parent
OUTPUT = HERE / 'ordercrew-site'
# Generated from the reviewed public source. Paths, encodings, sizes and hashes
# are independently fixed here as well as in both source documents.
ALLOWED = {'apple-touch-icon.png': {'bytes': 11795,
                          'encoding': 'base64',
                          'sha256': 'ea199f80e75335a561a9c086995d4114527db3805d6cbbbfaddfaf3ed1da73fd'},
 'assets/auth.css': {'bytes': 10321,
                     'encoding': 'utf-8',
                     'sha256': '665d10341a0bb94037fffa34123a0a9c9c555db271b005708beaa68805000e5f'},
 'assets/brand.svg': {'bytes': 1887,
                      'encoding': 'utf-8',
                      'sha256': '26e8d0aef8ca612a63d5bf1e540cbf6382d44823bb87d01fe7414318d4c6975f'},
 'assets/demo-access.js': {'bytes': 1634,
                           'encoding': 'utf-8',
                           'sha256': 'd3440d6ef511aaef8f699c2afb0156c2e6509409e25cb9d3353092ce4acc458a'},
 'assets/demo-locale.js': {'bytes': 614,
                           'encoding': 'utf-8',
                           'sha256': 'c4de9c31f629ecfca30d958503b13d28971309e3f0e93f03cfe0c497b15b0171'},
 'assets/forecast-model.js': {'bytes': 5642,
                              'encoding': 'utf-8',
                              'sha256': '75d764b9d5545064cb3378be6e2693863872026417428a3b7aebb399cf67c237'},
 'assets/forecast-view.css': {'bytes': 1789,
                              'encoding': 'utf-8',
                              'sha256': '9543c894bd8274991da6d596ab94d1561e1a7f2c8282c47891526a56e5f42547'},
 'assets/forecast-view.js': {'bytes': 8573,
                             'encoding': 'utf-8',
                             'sha256': '9753c533b40814d30d9f04e43bdf1fe8157fe9d485984abd54b9fbb09782fe76'},
 'assets/icons.svg': {'bytes': 12455,
                      'encoding': 'utf-8',
                      'sha256': 'df60d367bf536a7b2a8d8d1bf64d961c01e58267b684767af9ddff65b0be8a44'},
 'assets/login.js': {'bytes': 2206,
                     'encoding': 'utf-8',
                     'sha256': 'f68d0177c882ac2161fc53f12444caf3b5cb4251111a3cab9e55007016221f2d'},
 'assets/onboarding-content.js': {'bytes': 19323,
                                  'encoding': 'utf-8',
                                  'sha256': '754eb3fa210f3d257ecbc053d76bc6f0d037b3fa2e29e38842ce699b12a3a80e'},
 'assets/onboarding.css': {'bytes': 8246,
                           'encoding': 'utf-8',
                           'sha256': '9fd78b3f97e622458f814c67c451442ef835a02f344763bdbe5d4b0097e7e1af'},
 'assets/onboarding.js': {'bytes': 15335,
                          'encoding': 'utf-8',
                          'sha256': 'c8707f88a6e8ae5b6e797c64ab28e010e64bce675a01877c49dee35870f345e2'},
 'assets/site.css': {'bytes': 26799,
                     'encoding': 'utf-8',
                     'sha256': 'e3c557259e11d35b57b88fd9ffaa8051d3459b18ede0f83538ddeb2a6a6563fa'},
 'assets/site.en.js': {'bytes': 8383,
                       'encoding': 'utf-8',
                       'sha256': '350bee41df675ea6ee0a2fc7da400ba57aaf050a4427203659bb6ede2c60dcf6'},
 'assets/site.js': {'bytes': 8426,
                    'encoding': 'utf-8',
                    'sha256': 'df45ab5219720281f26dbd30c32d14d503b6147d3520f153238f9cc61a5588eb'},
 'assets/stijn-oudelaar.jpg': {'bytes': 54584,
                               'encoding': 'base64',
                               'sha256': '8bf30bd8244601e792312be0b7f562888f58963808fddeb6b3cfdec8f391332f'},
 'assets/thomas-winters.jpg': {'bytes': 60733,
                               'encoding': 'base64',
                               'sha256': 'd78f5be78272487cb91d6fd88c4d128896e14593af482ef19965259917773e5d'},
 'demo.html': {'bytes': 213163,
               'encoding': 'utf-8',
               'sha256': '0455620eab93c001235c05abab190097a9d47f272d01e87385180fdcee278f11'},
 'en/demo.html': {'bytes': 211892,
                  'encoding': 'utf-8',
                  'sha256': '810e6c8902cb49ea1c8e16c5830c59df8d1ad35d28abd9667584893dcc6b2091'},
 'en/index.html': {'bytes': 21303,
                   'encoding': 'utf-8',
                   'sha256': 'b37d5fe34d19dfdc727d7cf4f7a4a3cd160496fb82ce2cd709cca6dc0052a78a'},
 'en/login.html': {'bytes': 6270,
                   'encoding': 'utf-8',
                   'sha256': '453abdaa07ddd1a6365e526329fd7cbb3a86225fba915e3a9ea1e3a1ee52a356'},
 'en/onboarding.html': {'bytes': 7305,
                        'encoding': 'utf-8',
                        'sha256': 'b32ff11b9a3e31d274cd72e705d490060d27b8f319bda63f10ceb65934704c9d'},
 'en/privacy.html': {'bytes': 6583,
                     'encoding': 'utf-8',
                     'sha256': 'a86a7483ff4cd385e068e4d542f72458627b4d2ec6b288efdc9e115bc108a091'},
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
 'index.html': {'bytes': 21642,
                'encoding': 'utf-8',
                'sha256': '78776736c0a9aacecc7dfa3da2ccc4f04e27528e023489e8fb519a91dbe3542b'},
 'login.html': {'bytes': 6338,
                'encoding': 'utf-8',
                'sha256': 'b01f66361dae70f910d64688185d79fe2c696e37413ede27fbe418862ddb32a1'},
 'onboarding.html': {'bytes': 7490,
                     'encoding': 'utf-8',
                     'sha256': 'f742ce5161ea8b4a91513bd6915ec4d1748508b5418918532920bf24977061be'},
 'privacy.html': {'bytes': 6946,
                  'encoding': 'utf-8',
                  'sha256': 'e82e04c72ae2f5a82ab76c20eadb611f30cc53cd8061f7c1e3fec163750722bf'},
 'robots.txt': {'bytes': 70,
                'encoding': 'utf-8',
                'sha256': '85a0d28ee26c036fae7c4bd4f1fc9afd7ff0d0e46f00d9827343334ef44be6cb'},
 'site.webmanifest': {'bytes': 581,
                      'encoding': 'utf-8',
                      'sha256': '1124818aa8af8b7aaefd1254b544a3e65c900d98f4d54513124f59eb4f33d3eb'},
 'sitemap.xml': {'bytes': 271,
                 'encoding': 'utf-8',
                 'sha256': 'a72200a1c72a4e828927848c6f458cc7cc9866c6cee89ae6202433b5ec352f59'}}
SOURCES = {'site-source-demo-nl.json': {'part': 'demo-nl', 'paths': ['demo.html']},
 'site-source-en.json': {'part': 'en',
                         'paths': ['assets/site.en.js',
                                   'en/demo.html',
                                   'en/index.html',
                                   'en/login.html',
                                   'en/onboarding.html',
                                   'en/privacy.html']},
 'site-source-forecast.json': {'part': 'forecast',
                               'paths': ['assets/forecast-model.js',
                                         'assets/forecast-view.css',
                                         'assets/forecast-view.js']},
 'site-source-portraits.json': {'part': 'portraits',
                                'paths': ['assets/stijn-oudelaar.jpg',
                                          'assets/thomas-winters.jpg']},
 'site-source.json': {'part': 'nl-shared',
                      'paths': ['apple-touch-icon.png',
                                'assets/auth.css',
                                'assets/brand.svg',
                                'assets/demo-access.js',
                                'assets/demo-locale.js',
                                'assets/icons.svg',
                                'assets/login.js',
                                'assets/onboarding-content.js',
                                'assets/onboarding.css',
                                'assets/onboarding.js',
                                'assets/site.css',
                                'assets/site.js',
                                'favicon-48.png',
                                'favicon-96.png',
                                'favicon.ico',
                                'favicon.svg',
                                'icon-192.png',
                                'icon-512.png',
                                'index.html',
                                'login.html',
                                'onboarding.html',
                                'privacy.html',
                                'robots.txt',
                                'site.webmanifest',
                                'sitemap.xml']}}
RELEASE = 'OrderCrew verkoopverwachting 2026-11-18'
ARCHIVE_SHA256 = '69566cc5e99352d7bd7dfdbed1777d79d1d4d02a69c1ae702448ac144fb72f91'


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
    # Read and validate every partition before creating or changing any output.
    entries = []
    for filename, specification in SOURCES.items():
        source_path = HERE / filename
        require(not source_path.is_symlink() and source_path.resolve().is_relative_to(HERE),
                'Source path may not redirect: ' + filename)
        source = json.loads(source_path.read_text(encoding='utf-8'))
        require(isinstance(source, dict), 'Source document must be an object: ' + filename)
        require(source.get('format_version') == 2, 'Unsupported source format')
        require(source.get('release') == RELEASE, 'Unexpected source release')
        require(source.get('publish_directory') == 'ordercrew-site', 'Unexpected publish directory')
        require(source.get('reference_archive_sha256') == ARCHIVE_SHA256, 'Unexpected release archive')
        require(source.get('source_part') == specification['part'], 'Unexpected source partition')
        part_entries = source.get('files')
        require(isinstance(part_entries, list) and len(part_entries) == len(specification['paths']),
                'Unexpected source partition file count: ' + filename)
        require(all(isinstance(entry, dict) and isinstance(entry.get('path'), str) for entry in part_entries),
                'Invalid source partition entries: ' + filename)
        require(sorted(entry['path'] for entry in part_entries) == specification['paths'],
                'Source partition paths differ from reviewed paths: ' + filename)
        entries.extend(part_entries)
    require(len(entries) == len(ALLOWED), 'Unexpected public file count')
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
