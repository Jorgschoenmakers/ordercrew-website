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
 'assets/forecast-model.js': {'bytes': 5815,
                              'encoding': 'utf-8',
                              'sha256': 'c5d77e86489a317b75debaa63c6b545b74cb108033c65b5a218072e933339bdf'},
 'assets/forecast-view.css': {'bytes': 1789,
                              'encoding': 'utf-8',
                              'sha256': '9543c894bd8274991da6d596ab94d1561e1a7f2c8282c47891526a56e5f42547'},
 'assets/forecast-view.js': {'bytes': 8770,
                             'encoding': 'utf-8',
                             'sha256': 'accfd86265a77a9719f5dcde69006ec28eba84fce6f10aa7bd538576b08fb0d8'},
 'assets/icons.svg': {'bytes': 12455,
                      'encoding': 'utf-8',
                      'sha256': 'df60d367bf536a7b2a8d8d1bf64d961c01e58267b684767af9ddff65b0be8a44'},
 'assets/inventory-app.js': {'bytes': 7040,
                             'encoding': 'utf-8',
                             'sha256': '91c89c2981ddd0c576f14198b085f8cb195f019667b946a634fd8fcad18cb76e'},
 'assets/inventory-plan.js': {'bytes': 14110,
                              'encoding': 'utf-8',
                              'sha256': 'ef0d01e078e129c922604549e807ce81d537e9a879656681dcf67560b65fce26'},
 'assets/inventory-view.css': {'bytes': 5839,
                               'encoding': 'utf-8',
                               'sha256': 'dcce17623a0c1b5d433128eb6cffe50938e81e74dd3898c305ec6c63a2a67667'},
 'assets/inventory-view.js': {'bytes': 21500,
                              'encoding': 'utf-8',
                              'sha256': 'c099b85029f82d67d123e48e4f47df5057b857e92012cca7373b207c87f45c77'},
 'assets/login.js': {'bytes': 2206,
                     'encoding': 'utf-8',
                     'sha256': 'f68d0177c882ac2161fc53f12444caf3b5cb4251111a3cab9e55007016221f2d'},
 'assets/onboarding-content.js': {'bytes': 19367,
                                  'encoding': 'utf-8',
                                  'sha256': 'c0e9c0086d912f56e44aeca5e1d97cf14e2c40858006bb3ff713ba06d4fa636a'},
 'assets/onboarding.css': {'bytes': 8246,
                           'encoding': 'utf-8',
                           'sha256': '9fd78b3f97e622458f814c67c451442ef835a02f344763bdbe5d4b0097e7e1af'},
 'assets/onboarding.js': {'bytes': 15335,
                          'encoding': 'utf-8',
                          'sha256': 'c8707f88a6e8ae5b6e797c64ab28e010e64bce675a01877c49dee35870f345e2'},
 'assets/ordercrew-devices-en.webp': {'bytes': 64350,
                                      'encoding': 'base64',
                                      'sha256': '77bc018c1fa6b851b07ea0d023769d737b671deb9d78f6cd1549f51be98584e2'},
 'assets/ordercrew-devices-nl.webp': {'bytes': 68936,
                                      'encoding': 'base64',
                                      'sha256': '6e37e29285a5a86cca9d5368d3a0736ee4e0dcf097c5b071951ce37cb3fc3832'},
 'assets/site.css': {'bytes': 27627,
                     'encoding': 'utf-8',
                     'sha256': 'f35c4eacd640bc6a8a78d4173944a62473c118b7691129f5bdad5d9bee359a01'},
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
 'assets/zenchef.js': {'bytes': 16808,
                       'encoding': 'utf-8',
                       'sha256': 'b41c64a1c98e717e3bd9aa77c97d481b7c58e142b0b38db8426ff5e2ef16d580'},
 'demo.html': {'bytes': 212295,
               'encoding': 'utf-8',
               'sha256': 'c8595e04b18ddfe6473383042b53f93b5f322ef7041988cdd21b8b393058272d'},
 'en/demo.html': {'bytes': 211044,
                  'encoding': 'utf-8',
                  'sha256': 'c1d3ef8e6d90ce5459213f9cf8d47dc2fb744eccddf3b902f6c4511290d4cece'},
 'en/index.html': {'bytes': 21749,
                   'encoding': 'utf-8',
                   'sha256': '7bba42c6b2101d7456d907b9271a19eb5256e8284306920b773d2298ed2bbf78'},
 'en/login.html': {'bytes': 6270,
                   'encoding': 'utf-8',
                   'sha256': '453abdaa07ddd1a6365e526329fd7cbb3a86225fba915e3a9ea1e3a1ee52a356'},
 'en/onboarding.html': {'bytes': 7416,
                        'encoding': 'utf-8',
                        'sha256': '1231a17009dcf6511b5d5718c168d6f440a3a05d7d90943ea133bc2f0e0b090a'},
 'en/privacy.html': {'bytes': 6815,
                     'encoding': 'utf-8',
                     'sha256': 'f2e5b84c4ff10206a67481fdc23fc8e313abc35fd9135a101ec61eb777abdb8a'},
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
 'index.html': {'bytes': 22115,
                'encoding': 'utf-8',
                'sha256': 'b63d828d5205672037e9ce4d43334aed4fa2dd1eefe51e006e5c389693c29f50'},
 'login.html': {'bytes': 6338,
                'encoding': 'utf-8',
                'sha256': 'b01f66361dae70f910d64688185d79fe2c696e37413ede27fbe418862ddb32a1'},
 'onboarding.html': {'bytes': 7601,
                     'encoding': 'utf-8',
                     'sha256': 'be717243a2edb039163588a2bbe1c570ebfb7c977bde649a144caf7e5ba299fa'},
 'privacy.html': {'bytes': 7187,
                  'encoding': 'utf-8',
                  'sha256': '7f0597e50cac1cd17a6d9dd55525d1d4833e3848cc880ced5641e4000e02e310'},
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
 'site-source-devices.json': {'part': 'devices',
                              'paths': ['assets/ordercrew-devices-en.webp',
                                        'assets/ordercrew-devices-nl.webp']},
 'site-source-en.json': {'part': 'en',
                         'paths': ['en/demo.html',
                                   'en/login.html',
                                   'en/onboarding.html',
                                   'en/privacy.html']},
 'site-source-forecast.json': {'part': 'forecast',
                               'paths': ['assets/forecast-model.js',
                                         'assets/forecast-view.css',
                                         'assets/forecast-view.js',
                                         'assets/inventory-app.js',
                                         'assets/inventory-plan.js',
                                         'assets/inventory-view.css',
                                         'assets/inventory-view.js',
                                         'assets/zenchef.js']},
 'site-source-home.json': {'part': 'home',
                           'paths': ['assets/site.css',
                                     'assets/site.en.js',
                                     'assets/site.js',
                                     'en/index.html',
                                     'index.html']},
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
                                'favicon-48.png',
                                'favicon-96.png',
                                'favicon.ico',
                                'favicon.svg',
                                'icon-192.png',
                                'icon-512.png',
                                'login.html',
                                'onboarding.html',
                                'privacy.html',
                                'robots.txt',
                                'site.webmanifest',
                                'sitemap.xml']}}
RELEASE = 'OrderCrew Zenchef-reserveringen en apparaatweergave 2026-11-20'
ARCHIVE_SHA256 = 'e4c5fb4ed349533ea8bdcc34b569ccb9be78d1cd5d7869b43827e50f247361fc'


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
