# OrderCrew website

De homepage, gedeelde demo-inlog en voorbeeldkeuken worden gebouwd uit drie tekstbestanden die met de GitHub-webeditor kunnen worden bijgewerkt. Er zijn geen externe Python-pakketten nodig.

## Render-instellingen

Plaats `site-source.json`, `build_site.py` en dit `README.md` samen in de hoofdmap van de repository.

Build Command:

```sh
python3 build_site.py
```

Publish Directory:

```text
ordercrew-site
```

Het eerdere ZIP-bestand is voor deze build niet nodig. De builder leest of wijzigt dat ZIP-bestand niet.

## Controleerbare bron

`site-source.json` bevat precies de 20 openbare websitebestanden. HTML, CSS, JavaScript, SVG, XML en JSON staan als leesbare UTF-8-tekstregels in het bestand. Alleen de binaire PNG- en ICO-afbeeldingen gebruiken base64. Elke bronregel behoudt zijn oorspronkelijke regeleinde; de builder voegt de regels zonder extra tekens samen.

Voor elk bestand staan pad, bytegrootte en SHA256 in de bron. De builder controleert eerst alle twintig bestanden op de vaste allowlist, veilige paden, grootte en hash. Pas daarna schrijft hij onder `ordercrew-site/`, met een tweede hashcontrole van de geschreven bestanden. Onverwachte bestanden of symlinks worden geweigerd. De builder verwijdert niets en schrijft niet buiten zijn uitvoermap.

De bestandsbytes zijn gelijk aan de gecontroleerde release van 27 oktober 2026. De homepage behoudt de Google-verificatietag, canonical en sitemap. Login, demo en privacy blijven `noindex`. Het bestaande OrderCrew-logo staat in de faviconformaten; Google bepaalt zelf wanneer zoekresultaten worden bijgewerkt. CSS- en JavaScript-links gebruiken inhoudsversies om oude browsercache te voorkomen.

## Grenzen van de demo

De voorbeeldkeuken gebruikt fictieve gegevens en lokale browseropslag. De bestaande gedeelde demo-inlog is een demo-toegangsscherm, geen serverbeveiliging voor privégegevens. Er worden geen echte bestellingen verstuurd en er is geen live DISH-koppeling. Er zijn geen hosting-, GitHub- of persoonlijke accountgegevens toegevoegd.

Een geslaagde lokale build bewijst de bestandsinhoud. De daadwerkelijke Render-uitrol, HTTPS-routes en browserwerking moeten na publicatie afzonderlijk worden gecontroleerd.
