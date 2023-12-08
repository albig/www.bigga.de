---
tags: typo3, osm, opensource
date: 2023-10-08
language: de
category: typo3
---

# Neues Release von EXT:ods_osm - OpenStreetMap in TYPO3

## OpenStreetMap als Hobby-Projekt

Als kleines Hobby-Projekt kümmere ich mich um die TYPO3-Extension "ods_osm". Mit der Extension kann man sich eine OpenStreetMap-Karte als Inhaltselment in seine TYPO3-Seite(n) einbauen, dort z.B. Marker anzeigen, die man anklicken kann. Keine Raketentechnik möchte man meinen, weil das gibt's ja seit Google Maps - also seit gut 20 Jahren. Praktisch ist es aber immer noch.

Gute Karten-Daten sind unglaublich nützlich. Und diese Daten selbst korrigieren und ergänzen zu können, macht einen großen Reiz für mich aus. Ich bin immer mit StreetComplete (Android App um spielerisch fehlende Daten in OpenStreetMap zu erfassen), Vespucci (Android Editor für OpenStreetMap) und OsmAnd (OpenStreetMap App für Android) unterwegs. Immer nur so viel, wie gerade möglich ist. Denn Daten erfassen kann man unendlich ausweiten.

## Open-Source Projekt gerettet

Die Extension stellt die JavaScript-Bibliotheken bereit, die die Karten-Daten anzeigen kann. Unterstützt wird Leaflet und OpenLayers. Ein Redakteur kann Marker, Tracks als GPX und KML und Vektordaten im GeoJSON-Format als Ebene auf der Karte anzeigen lassen.

Anfang 2020 hatte ich den Autor und Maintainer der Extension, Robert Heel, angeschrieben und gefragt, ob es bald ein Release für TYPO3 9 LTS geben wird und ob ich ihn ggf. unterstützen kann. Daraus ist geworden, dass ich seitdem die Entwicklung übernommen habe, was hauptsächlich bedeutet, die Extension für die aktuellen TYPO3-Versionen anzupassen und die vorhandenen JavaScript-Bibliotheken zu aktualisieren.

Robert ist weiterhin Owner der Extension, des GitHub-Repos und des TER-Accounts. Und ich freu mich, dass ich viel lernen konnte, dieses Stückchen Open-Source Software nun schon bald 4 Jahre weiter leben konnte und dem ein oder anderen Nutzer nützlich war und dass Robert nach wie vor die Releases im TER veröffentlicht.

## Demo-Seite für ods_osm

Vor einer Weile habe ich eine Demo-Seite unter [https://osm.bigga.de](https://osm.bigga.de) für ods_osm angefangen um zu zeigen, was die Extension alles kann. Das ist ja durchaus auch etwas mühsam zusammen zu klicken. Aber wenn man das Ergebnis sieht, nimmt man den Weg eher auf sich.

Die Seite zeigt noch nicht alles. Anregungen sind herzlich willkommen.


## ods_osm Version 4.2.0

Neu an der Version 4.2.0 ist vor allem die Kompatibilität mit TYPO3 12.4 LTS und damit auch mit PHP 8.2. Dazu hab ich OpenLayers auf die Version 8.1.0 aktualisiert.

Ein kleines Feature ist dazu gekommen. Man kann nun die Properties von GeoJSON-Daten in einem Popup anzeigen lassen. Beispielsweise kann man in einer Karte alle Wahlkreise zur Kommunalwahl 2024 anklicken und bekommt die Wahlkreis-Nummer. Wenn ich mir dann noch mal die Mühe mache, die Stadtteile in den Properites hinzuzufügen, dann würde mann die auch sehen.

Beispiel: [https://osm.bigga.de/examples/leaflet/geojson/kommunalwahlkreise-dresden-2024](https://osm.bigga.de/examples/leaflet/geojson/kommunalwahlkreise-dresden-2024)

```{figure} ods-osm-4-2-0-2023-10-08_22-48.png
:alt: Screenshot aus dem TYPO3 Extension Repository (TER) zur Extension `ods_osm`. Zu lesen ist, dass die neue Version 4.2.0 von Robert Heel am 07.10.2023 hochgeladen wurde. Sie liegt in kompatiblen Versionen für TYPO3 seit 4.5 LTS und bis 12.4 LTS vor.
:class: with-shadow
:width: 800px
:align: left

Screenshot aus dem TYPO3 Extension Repository (TER) zur Extension `ods_osm`
```

Die Extension ist hier zu finden:

* GitHub: [https://github.com/bobosch/ods_osm](https://github.com/bobosch/ods_osm)
* TYPO3 Extension Repository (TER): [https://extensions.typo3.org/extension/ods_osm](https://extensions.typo3.org/extension/ods_osm)
* Packagist: [https://packagist.org/packages/bobosch/ods-osm](https://packagist.org/packages/bobosch/ods-osm)
* Dokumentation: [https://docs.typo3.org/p/bobosch/ods-osm/4.2/en-us/](https://docs.typo3.org/p/bobosch/ods-osm/4.2/en-us/)

## Weitere Entwicklung

Ich wollte mir schon lange mal die Mühe machen, und die Extension auf Fluid umzustellen. Das Mischmasch aus PHP und JavaScript-Code ist alles andere als leicht zu maintainen. Auch muss man manchmal das JavaScript komplizierter machen, als es ist, weil es sonst nicht durch die Programmlogik abbildbar ist.

Irgendwann ist dann auch die Beschäftigung mit TYPO3 13 dran. So lange mir da aber der Anwendungsfall fehlt, setz ich mich da sicher nicht dran.

Jetzt wart ich mal ab, was nach dem Release an kleinen oder großen Fehlern über GitHub gemeldet wird. Die werde ich natürlich zügig beheben. Noch cooler wäre es natürlich, wenn ich fertige Pull-Requests bekommen würde.

Zu tun bleibt auf jeden Fall genug.
