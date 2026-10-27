# OrderCrew Render package

Prepared from approved Sites v2 source commit `905cd0d62c75e23c2410165e0b74d456faea490c`.
The original Sites checkout and published Sites deployment are unchanged.

## Render deployment

Put `ordercrew-render-site.zip` at the root of the existing Render-linked Git repository.
Build command:

```sh
python3 -c "import zipfile; zipfile.ZipFile('ordercrew-render-site.zip').extractall('.')"
```

Publish directory: `ordercrew-site`

The archive contains only `ordercrew-site/` and its public static assets. The README and
manifest are outside the public directory and are not included in the archive.
The existing Render SPA rewrite should be checked: real files must resolve directly,
and `/login` or `/demo` should not accidentally return the landing page. Explicit
`login.html` and `demo.html` links are supplied in all authored navigation.

## Scope

- Preserves landing page, login, demo, privacy, local storage behavior and styling.
- Open Graph origin changed to `https://www.ordercrew.nl`.
- Privacy hosting reference changed from ChatGPT Sites to Render.
- No external tracking scripts or fonts added.
- The login is a browser-local demo flow, not production authentication.
- Existing demo credentials and noindex/robots behavior are preserved.
- No `.git`, `.openai`, hosting credentials or user business data are included.

## Archive integrity

SHA-256: `593cf822427bef1e784fa5a756a328df053d7fbe278f0d34cbbdd9cd1c9b696e`

## Public file manifest

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| `assets/auth.css` | 7314 | `bfddabba13a96236307b245f8bb956d66e91051c372e8a6f0bb2cb9aa1586aa0` |
| `assets/brand.svg` | 341 | `fb94ffaaeff340f90476450d840f06e293b7f17058bd8dca95e7bcd05112e95f` |
| `assets/demo-access.js` | 1578 | `666b9ecb75fb602cb4ec30bedc1910dd18db25e5f29a3437630e580c0c19a10a` |
| `assets/login.js` | 1662 | `10895f3dd7fe25c697147faa59749e3ab9ae1c8c81ecd49cb5531bbfc52ba56f` |
| `assets/site.css` | 30245 | `ef907588063d22760a27907f53f0bcd57ad102be74097ff97e9dbcf84f8cf024` |
| `assets/site.js` | 3635 | `83577667ed4e0ba58e1ab8293a72f3cc375fd1acf9976e1ac63a591bfbcc57d1` |
| `demo.html` | 212247 | `1b3e3ab55f54e47ec3c942b89fc795367e459fd25aa3c17fa2bd989ac18dcaf0` |
| `index.html` | 15388 | `c14642608c534cea9aef16c5d447fde253a9dc58972190c999b9b6d50b32ddc9` |
| `login.html` | 4307 | `e2abc867becc78a7f997eecd09711dcc5d443190377afc176d6f7e0fbfbd70f3` |
| `privacy.html` | 4688 | `3a5c4092d60495465a42310d73854cf97e944379b945b5f9c995b440b7745f1e` |
| `robots.txt` | 26 | `331ea9090db0c9f6f597bd9840fd5b171830f6e0b3ba1cb24dfa91f0c95aedc1` |
