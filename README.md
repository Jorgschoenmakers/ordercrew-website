# OrderCrew website

Plaats `site-source.json`, `site-source-demo-nl.json`, `site-source-en.json`, `site-source-portraits.json`, `site-source-forecast.json`, `build_site.py` en `README.md` samen in de hoofdmap van de GitHub-repository.

Render Build Command blijft:

```sh
python3 build_site.py
```

Render Publish Directory blijft `ordercrew-site`.

De bron bevat 41 openbare bestanden, verdeeld over vijf bronbestanden van elk minder dan 300000 bytes. De Nederlandse en Engelse demo gebruiken dezelfde prognose, voorraadberekening en partij-editor uit `site-source-forecast.json`. De overige vier bronbestanden bevatten de Nederlandse en gedeelde bestanden, de Nederlandse demo, de Engelse versie en de portretfoto's. De builder controleert de bestandsnamen, groottes, SHA256-hashes en archiefreferentie voordat hij de site onder `ordercrew-site/` schrijft.

Het oudere ZIP-bestand in deze repository is historisch en wordt niet gebouwd. Het afzonderlijk opgeleverde releasepakket (`upload/ordercrew-render-site.zip`) heeft SHA256: `89158ce7b1f8551143bdd18a722b50cf80cf3d8d8eead0dbf592cc29f667541e`.

De Nederlandse en Engelse homepages verwijzen naar de onboarding voor pilotklanten. De zeven stappen staan in `onboarding.html` en `en/onboarding.html`. De checklist, notities en feedback worden lokaal in de browser bewaard. Deelnemers kunnen hun gegevens downloaden om die zelf te delen. De twee talen gebruiken dezelfde voortgang.

De demo berekent met fictieve reserveringen, historische opkomst en historische verkoop een prognose voor morgen en een voor het hele weekend. De chef kan de opkomst of een apart gerecht bijstellen. De standaard bereidingsmarge is 0%. Voor gebruik van restaurantgegevens zijn toegang tot Zenchef en historische kassaverkoop nodig.

De chef kiest per product de bestelperiode en kan de getelde voorraad over partijen verdelen. OrderCrew rekent per geplande gebruiksdag met de beschikbare hoeveelheid, uiterste gebruiksdatum en ingevulde ontdooitijd. De mise-en-place toont wanneer en hoeveel de keuken moet ontdooien. De leverancierslijst toont het resterende tekort en rondt de bestelling af op hele verpakkingen. Partijen en aanpassingen in deze demo worden lokaal in de browser bewaard.

Een lokale build bewijst de bestandsinhoud. Render-publicatie, domein/TLS, browserwerking en het Google-zoekresultaat worden daarna afzonderlijk gecontroleerd.

## Productvisualisaties van 19 november 2026

Alleen de Nederlandse homepage krijgt apparaatbeelden en een videosectie. De bestaande navigatie, teksten, kleuren, het lettertype, demo en andere pagina’s blijven behouden. `site-source-product-images.json` en `site-source-product-video.json` leveren de extra media en geïsoleerde CSS. De oorspronkelijke archiefreferentie blijft de referentie naar de basisrelease; de allowlist bevat bijgewerkte hashes voor de homepage en nieuwe media.

De 29 seconden durende video toont echte schermbeelden met voorbeeldgegevens en heeft geen geluid. Het is een gemonteerde schermpresentatie, geen gefilmde praktijktest. De huidige demo bewaart wijzigingen lokaal en verzendt geen echte orders.
