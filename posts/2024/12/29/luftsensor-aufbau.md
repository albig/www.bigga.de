---
tags: basteln, elektronik, citizen science
date: 2024-12-29
language: de
category: basteln
---

# Luftdaten-Sensor zusammengebaut

Heute habe ich endlich die Einzelteile des Luftdaten-Sensors zusammengebaut, die Firmware geflashed, den Sensor aufgehängt und im Sensor-Netz angemeldet.

Zeitaufwand: ca. 1 Stunde!

Gekauft hatte ich die Komponenten [im November über AliExpress](/posts/2024/11/30/meine-erste-aliexpress.md).

## Firmware flashen

Vor dem Zusammenbau des ganzen Sensors sollte man [laut Anleitung](https://sensor.community/de/sensors/airrohr/) die Firmware auf das ESP8266-Prozessorboard spielen.

Mit dem "AirRohr Firmware-Flasher" ging das mit der Linux-Version völlig problemlos. Programm mit `sudo` starten, ESP8266-Board verbinden, Programm hochladen. Fertig.

## Zusammenbau

Nur beim BME280-Sensor muss die Stiftleiste angelötet werden. Aber das war dann schon die größte Herausforderung. Mit den Kabeln noch die richtigen PINs verbinden, Prozessor-Board und Partikel-Sensor verbinden, alles in die zwei Abflussrohre stecken. Fertig.

## Im WLAN anmelden

Damit die gemessenenen Daten abgerufen werden können bzw. selbst den Weg ins Sensor-Netz finden, braucht der Luftdaten-Sensor einen Zugang zum Internet über WLAN. Unser WLAN-Router ist zum Glück stark genug, dass er der Sensor am vorgesehenen Standort Empfang hat.

Wenn der Sensor keinen Zugriff auf's WLAN hat, macht er selbst eine WLAN-Access-Point auf. Darüber kann man sich dann verbinden und das ESP8266-Board konfigurieren. So einfach!

## Im Sensor-Netz anmelden

Auch die Anmeldung des Sensors im [https://sensor.community/](Sensor-Netz) ist sehr einfach. Man registriert sich mit der E-Mail-Adresse und fügt den Sensor mit seiner Sensor-ID hinzu. Die Sensor-ID selbst bekommt man aus dem Namen des WLAN-Netz, was der Sensor für die Konfiguration aufgemacht hatte. Keine Ahnung, woher er die ID nimmt.

```{thumbnail} karte-senor-community-2024-12-29_25.png
:alt: Screenshot von der Seite sensor.community. Karte von Dresden mit Waben in unterschiedlicher Farbe von grün bis rot.
:class: with-shadow
:width: 350px
:align: left

Auf der Seite sensor.community findet man meinen Sensor in Löbtau seit 29.12.2024.
```

## Sensor aufhängen

Den Standort hatte ich mir natürlich vorher überlegt. Empfohlen wird 1-1,5m über dem Boden in der nähe der Straße. Das kann ich nun nicht bieten. Dafür hängt der Sensor jetzt geschützt vor der Sonne unter der Markise auf dem Nord-Balkon. Hier ist WLAN-Empfang und in 3m Entfernung mit einem USB-Flachbandkabel durch das Küchenfenster hab ich Zugang zum Stromnetz.

## Lokaler Abruf der Sensor-Daten

```{thumbnail} screenshot-sensor-2024-12-29_21-04.png
:alt: Screenshot von der lokalen Webseite des Luftdaten-Sensors mit den aktuellen Messwerten.
:class: with-shadow
:width: 350px
:align: left

Im lokalen Netz kann man direkt auf die Webseite des Luftdaten-Sensors zugreifen.
```

## Fazit

Der Aufbau war wirklich easy und kann ich auch für Einsteiger empfehlen. Klar, sind mir manche Vorgänge sehr vertraut und musste da nicht lange drüber nachdenken (Löten, Verbinden, Flashen, Konfigurieren...). Aber dass alles auf Anhieb funktionierte, hat mich doch erstaunt.

Bin gespannt, wie sich die Werte entwickeln. Im dritten Stock sind die Feinstaubwerte ja vielleicht grundsätzlich besser. Aber auch hier wird die schlechte Luft zu Silvester vorbeikommen. Auf die Werte bin ich besonders gespannt. Drum wollte ich das unbedingt noch vor dem 31.12. erledigt haben

Hier geht's zur [Karte it meinem Sensor im Sensor-Netz](https://maps.sensor.community/#14/51.0449/13.6814).