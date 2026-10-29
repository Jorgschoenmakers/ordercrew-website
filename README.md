# OrderCrew website

Plaats `site-source.json`, `site-source-en.json`, `site-source-portraits.json`, `build_site.py` en `README.md` samen in de hoofdmap van de GitHub-repository.

Render Build Command blijft:

```sh
python3 build_site.py
```

Render Publish Directory blijft `ordercrew-site`.

De bron bevat 29 openbare bestanden, verdeeld over drie bronbestanden van elk minder dan 500000 bytes voor betrouwbare browserpublicatie. `site-source.json` bevat Nederlands en gedeelde bestanden, behalve de portretten; `site-source-en.json` bevat de Engelse pagina's en `assets/site.en.js`; `site-source-portraits.json` bevat uitsluitend `assets/thomas-winters.jpg` en `assets/stijn-oudelaar.jpg`. HTML, CSS, JavaScript, SVG en andere tekst staan als leesbare UTF-8-regels in JSON. Alleen binaire media worden base64 gecodeerd. De builder gebruikt alleen Python-stdlib, leest alle drie de bronbestanden en controleert eerst formaat, release, partitie, archiefreferentie, exact toegestane paden, alle bytegroottes en SHA256-hashes. Pas daarna schrijft hij onder `ordercrew-site/`. Hij verwijdert niets en weigert onverwachte bestanden of doorverwijzende paden. Gebruik een schone build als een oude uitvoermap onverwachte bestanden bevat.

Het oudere ZIP-bestand in deze repository is historisch en wordt niet gebouwd. Het afzonderlijk opgeleverde releasepakket (`upload/ordercrew-render-site.zip`) heeft SHA256: `d91f3ce5be208d255411228e9c42ebcabfe2e92019a10f52de3e3af554acafc1`.

De Nederlandstalige en Engelstalige pagina's staan respectievelijk in de hoofdmap en onder `en/`. De taalkeuze gebruikt gewone links. Beide homepages zijn indexeerbaar; login, demo en privacy blijven noindex. De over-ons-informatie bevat de bevestigde namen Thomas Winters en Stijn Oudelaar met hun portretten; biografische informatie is nog niet aangeleverd. De herkomstregistratie van de portretten blijft buiten de openbare bestanden.

De app gebruikt voorbeeldgegevens. De gedeelde demo-inlog is geen serverbeveiliging voor persoonlijke gegevens; er worden geen echte bestellingen verzonden en er is geen live kassakoppeling. De producttour is een interactieve presentatie. Alleen een afzonderlijk meegeleverd afspeelbaar videobestand mag als video worden beschreven.

Een lokale build bewijst de bestandsinhoud. Render-publicatie, domein/TLS, browserwerking en het Google-zoekresultaat worden daarna afzonderlijk gecontroleerd.
