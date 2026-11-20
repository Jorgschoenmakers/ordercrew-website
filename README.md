# OrderCrew website

Deze release van 20 november 2026 toont de voorbeeldkeuken op laptop, tablet en telefoon op beide homepages. Vanuit de voorbeeldkeuken kan een chef Zenchef-reserveringen aanleveren voor de prognose.

## Publiceren op Render

Plaats `build_site.py`, deze README en de volgende bestanden samen in de hoofdmap van de GitHub-repository.

- `site-source.json` bevat Nederlandse en gedeelde bestanden.
- `site-source-demo-nl.json` bevat Nederlandse voorbeeldkeuken.
- `site-source-en.json` bevat Engelse voorbeeldkeuken en overige Engelse pagina’s.
- `site-source-forecast.json` bevat prognose, voorraadplanning en Zenchef-reserveringen.
- `site-source-portraits.json` bevat portretten.
- `site-source-home.json` bevat homepages met hun stijl en interactie.
- `site-source-devices.json` bevat apparaatbeelden van de Nederlandse en Engelse demo.

Render gebruikt deze bouwopdracht.

```sh
python3 build_site.py
```

De publicatiemap is `ordercrew-site`.

De bouwbron bevat 44 openbare bestanden in 7 JSON-bestanden. De builder controleert voor het schrijven de paden, inhoud, bestandsgrootte, SHA256-hashes en referentie naar het releasearchief.

Het releasepakket `upload/ordercrew-render-site.zip` heeft SHA256 `e4c5fb4ed349533ea8bdcc34b569ccb9be78d1cd5d7869b43827e50f247361fc`. Het ZIP-bestand dat nog in de GitHub-repository staat hoort bij een eerdere release.

De Nederlandse en Engelse homepages verwijzen naar de onboarding voor pilotklanten. De zeven stappen staan in `onboarding.html` en `en/onboarding.html`. De checklist, notities en feedback worden lokaal in de browser bewaard. Deelnemers kunnen hun gegevens downloaden om die zelf te delen. De twee talen gebruiken dezelfde voortgang.

De demo berekent voor morgen en voor het hele weekend een prognose met voorbeeldcijfers voor opkomst en verkoop. Een CSV-import uit Zenchef kan de voorbeeldreserveringen voor de gekozen periode vervangen. De chef kan de opkomst of een apart gerecht bijstellen. De standaard bereidingsmarge is 0%. Voor automatische synchronisatie is API-toegang van het restaurant nodig.

De chef kiest per product de bestelperiode en kan de getelde voorraad over partijen verdelen. OrderCrew rekent per geplande gebruiksdag met de beschikbare hoeveelheid, uiterste gebruiksdatum en ingevulde ontdooitijd. De mise-en-place toont wanneer en hoeveel de keuken moet ontdooien. De leverancierslijst toont het resterende tekort en rondt de bestelling af op hele verpakkingen. Partijen en aanpassingen in deze demo worden lokaal in de browser bewaard.

Een lokale build bewijst de bestandsinhoud. Render-publicatie, domein/TLS, browserwerking en het Google-zoekresultaat worden daarna afzonderlijk gecontroleerd.
