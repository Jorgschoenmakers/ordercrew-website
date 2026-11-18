# OrderCrew website

Plaats `site-source.json`, `site-source-demo-nl.json`, `site-source-en.json`, `site-source-portraits.json`, `build_site.py` en `README.md` samen in de hoofdmap van de GitHub-repository.

Render Build Command blijft:

```sh
python3 build_site.py
```

Render Publish Directory blijft `ordercrew-site`.

De bron bevat 34 openbare bestanden, verdeeld over vier bronbestanden van elk minder dan 300000 bytes voor betrouwbare browserpublicatie. `site-source.json` bevat Nederlands en gedeelde bestanden, behalve de demo en portretten; `site-source-demo-nl.json` bevat uitsluitend `demo.html`; `site-source-en.json` bevat de Engelse pagina's en `assets/site.en.js`; `site-source-portraits.json` bevat uitsluitend `assets/thomas-winters.jpg` en `assets/stijn-oudelaar.jpg`. HTML, CSS, JavaScript, SVG en andere tekst staan als leesbare UTF-8-regels in JSON. Alleen binaire media worden base64 gecodeerd. De builder gebruikt alleen Python-stdlib, leest alle vier de bronbestanden en controleert eerst formaat, release, partitie, archiefreferentie, exact toegestane paden, alle bytegroottes en SHA256-hashes. Pas daarna schrijft hij onder `ordercrew-site/`. Hij verwijdert niets en weigert onverwachte bestanden of doorverwijzende paden. Gebruik een schone build als een oude uitvoermap onverwachte bestanden bevat.

Het oudere ZIP-bestand in deze repository is historisch en wordt niet gebouwd. Het afzonderlijk opgeleverde releasepakket (`upload/ordercrew-render-site.zip`) heeft SHA256: `da1ae249d457b19befbe03bbae1580416a44c452b69ca42d85576da0fa2e9bd0`.

De Nederlandse en Engelse homepages verwijzen naar de onboarding voor pilotklanten. De zeven stappen staan in `onboarding.html` en `en/onboarding.html`. De checklist, notities en feedback worden lokaal in de browser bewaard. Deelnemers kunnen hun gegevens downloaden om die zelf te delen. De twee talen gebruiken dezelfde voortgang.

De demo werkt met voorbeeldgegevens. De chef controleert een besteladvies en bestelt via de gebruikelijke route.

Een lokale build bewijst de bestandsinhoud. Render-publicatie, domein/TLS, browserwerking en het Google-zoekresultaat worden daarna afzonderlijk gecontroleerd.
