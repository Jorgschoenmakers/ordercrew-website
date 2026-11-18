# OrderCrew website

Plaats `site-source.json`, `site-source-demo-nl.json`, `site-source-en.json`, `site-source-portraits.json`, `site-source-forecast.json`, `build_site.py` en `README.md` samen in de hoofdmap van de GitHub-repository.

Render Build Command blijft:

```sh
python3 build_site.py
```

Render Publish Directory blijft `ordercrew-site`.

De bron bevat 37 openbare bestanden, verdeeld over vijf bronbestanden van elk minder dan 300000 bytes. De twee demo's delen dezelfde berekening en weergave in `site-source-forecast.json`. De overige partities bevatten respectievelijk de Nederlandse en gedeelde bestanden, de Nederlandse demo, de Engelse versie en de portretfoto's. De builder controleert de bestandsnamen, groottes, SHA256-hashes en archiefreferentie voordat hij de site onder `ordercrew-site/` schrijft.

Het oudere ZIP-bestand in deze repository is historisch en wordt niet gebouwd. Het afzonderlijk opgeleverde releasepakket (`upload/ordercrew-render-site.zip`) heeft SHA256: `69566cc5e99352d7bd7dfdbed1777d79d1d4d02a69c1ae702448ac144fb72f91`.

De Nederlandse en Engelse homepages verwijzen naar de onboarding voor pilotklanten. De zeven stappen staan in `onboarding.html` en `en/onboarding.html`. De checklist, notities en feedback worden lokaal in de browser bewaard. Deelnemers kunnen hun gegevens downloaden om die zelf te delen. De twee talen gebruiken dezelfde voortgang.

De demo berekent met fictieve reserveringen, historische opkomst en historische verkoop een prognose voor morgen en een voor het hele weekend. De chef kan de opkomst of een apart gerecht bijstellen. De standaard bereidingsmarge is 0%. Voor gebruik van restaurantgegevens zijn toegang tot Zenchef en historische kassaverkoop nodig.

Een lokale build bewijst de bestandsinhoud. Render-publicatie, domein/TLS, browserwerking en het Google-zoekresultaat worden daarna afzonderlijk gecontroleerd.
