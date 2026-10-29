# OrderCrew website

Plaats `site-source.json`, `site-source-en.json`, `build_site.py` en `README.md` samen in de hoofdmap van de GitHub-repository.

Render Build Command blijft:

```sh
python3 build_site.py
```

Render Publish Directory blijft `ordercrew-site`.

De bron bevat 27 openbare bestanden, verdeeld over twee bronbestanden van elk minder dan 500000 bytes voor betrouwbare browserpublicatie. `site-source.json` bevat Nederlands en gedeelde bestanden; `site-source-en.json` bevat de Engelse pagina's en `assets/site.en.js`. HTML, CSS, JavaScript, SVG en andere tekst staan als leesbare UTF-8-regels in JSON. Alleen binaire media worden base64 gecodeerd. De builder gebruikt alleen Python-stdlib, leest beide bronbestanden en controleert eerst formaat, release, partitie, archiefreferentie, exact toegestane paden, alle bytegroottes en SHA256-hashes. Pas daarna schrijft hij onder `ordercrew-site/`. Hij verwijdert niets en weigert onverwachte bestanden of doorverwijzende paden. Gebruik een schone build als een oude uitvoermap onverwachte bestanden bevat.

Het oudere ZIP-bestand in deze repository is historisch en wordt niet gebouwd. Het afzonderlijk opgeleverde releasepakket (`upload/ordercrew-render-site.zip`) heeft SHA256: `63701dac47bf4984a57ada4d6e6e9601279ff20572106ff144e6185ab0d6b75c`.

De Nederlandstalige en Engelstalige pagina's staan respectievelijk in de hoofdmap en onder `en/`. De taalkeuze gebruikt gewone links. Beide homepages zijn indexeerbaar; login, demo en privacy blijven noindex. De over-ons-informatie bevat alleen de bevestigde namen Thomas Winters en Stijn Oudelaar; biografische informatie is nog niet aangeleverd.

De app gebruikt voorbeeldgegevens. De gedeelde demo-inlog is geen serverbeveiliging voor persoonlijke gegevens; er worden geen echte bestellingen verzonden en er is geen live kassakoppeling. De producttour is een interactieve presentatie. Alleen een afzonderlijk meegeleverd afspeelbaar videobestand mag als video worden beschreven.

Een lokale build bewijst de bestandsinhoud. Render-publicatie, domein/TLS, browserwerking en het Google-zoekresultaat worden daarna afzonderlijk gecontroleerd.
