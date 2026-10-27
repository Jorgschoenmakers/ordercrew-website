# OrderCrew website

De openbare homepage beschrijft OrderCrew en leidt via de demo-inlog naar een voorbeeldkeuken. De demo verwerkt uitsluitend voorbeeldgegevens lokaal in de browser; er worden geen echte bestellingen verstuurd en er is geen live DISH-koppeling.

Deze release maakt de homepage crawlbaar, voegt een canonical naar `https://www.ordercrew.nl/`, feitelijke WebSite/Organization-gegevens en een sitemap met alleen de homepage toe. Login, demo en privacy behouden `noindex`. De homepage bevat daarnaast de openbare Google Search Console-verificatietag. Google-verificatie, sitemapverwerking en indexering moeten afzonderlijk worden gecontroleerd; deze release garandeert geen opname of positie in zoekresultaten.

Render build command:

```sh
python3 -c "import zipfile; zipfile.ZipFile('ordercrew-render-site.zip').extractall('.')"
```

Publish directory: `ordercrew-site`.

`ordercrew-render-site.zip` bevat 12 openbare bestanden en is 78.919 bytes groot. De demo, inlog, styling en overige applicatiebestanden zijn byte-identiek aan de eerdere Render-release. Lokale controles op de indexeringsregels, canonical, sitemap, structured data, exacte verificatietag en pakketintegriteit zijn geslaagd.

SHA-256: `42b367c78bdd791902df3967cf917d8757a6e9748657f5f34e368d3978045ba7`.
