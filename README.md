# OrderCrew website

Plaats `site-source.json`, `build_site.py` en `README.md` samen in de hoofdmap van de GitHub-repository.

Render Build Command blijft:

```sh
python3 build_site.py
```

Render Publish Directory blijft `ordercrew-site`.

De bron bevat 21 openbare bestanden. HTML, CSS, JavaScript, SVG en andere tekst staan als leesbare UTF-8-regels in JSON. Alleen binaire media worden base64 gecodeerd. De builder gebruikt alleen Python-stdlib, accepteert uitsluitend de exact gegenereerde allowlist en controleert alle bytegroottes en SHA256-hashes voor het schrijven. Hij schrijft uitsluitend onder `ordercrew-site/`, verwijdert niets en weigert onverwachte bestanden of doorverwijzende paden. Gebruik een schone build als een oude uitvoermap onverwachte bestanden bevat.

Het oudere ZIP-bestand in deze repository is historisch en wordt niet gebouwd. Het afzonderlijk opgeleverde releasepakket (`upload/ordercrew-render-site.zip`) heeft SHA256: `f7aa6e9d3e99b3babccd603338e9110b61f829862d78f08f319e2040915a4a9a`.

De app gebruikt voorbeeldgegevens. De gedeelde demo-inlog is geen serverbeveiliging voor persoonlijke gegevens; er worden geen echte bestellingen verzonden en er is geen live kassakoppeling. De producttour is een interactieve presentatie. Alleen een afzonderlijk meegeleverd afspeelbaar videobestand mag als video worden beschreven.

Een lokale build bewijst de bestandsinhoud. Render-publicatie, domein/TLS, browserwerking en het Google-zoekresultaat worden daarna afzonderlijk gecontroleerd.
