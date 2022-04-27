---
tags: linux, jolla, sailfish, eos
date: 2022-04-22
language: de
category: software
---

# Ich wechsle mal das Handy-Betriebsssytem: Sailfish -> /e/OS

Seit Oktober 2020 habe ich ein Sony Xperia XA2. Gebraucht gekauft bei [Smallbug.de](https://smallbug.de) für 123 €. Das originale Android Betriebssystem war aber nie mein Ziel. Sondern ich hatte es gleich mit Sailfish OS geflasht. Gut, das hat dann nochmal 50 € für die Sailfish-Lizenz dazu. Soweit so schick. Android-Apps laufen bis zu einem gewissen Grad ja trotzdem unter Sailfish.

Seit dem Release 4.3.0 hatte ich dann plötzlich Probleme mit Osmand und anderen Android Apps. Osmand friert plötzlich ein und die gesamte Android-Virtualisierung startet sich neu, was 1-3 Minuten dauert. Nicht gerade praktisch.

Mit dem Release 4.4.0 wurde es nicht besser und so richtig scheint das Problem außer mir keiner zu haben. Also ist das Handy hinüber? Oder hat es was damit zu tun, dass ich damit von Android 8 auf Sailfish umgestiegen bin? Es ist mir bis heute unklar, was die originale Android-Version für Auswirkungen hat.

Vor [10 Tagen hab ich das Handy komplett neu mit Sailfish OS 4.4 geflasht](http://www.bigga.de/posts/2022/04/12/sailfish-reflash-sony-xa2/). Aber das Verhalten hat sich gar nicht verbessert.

Gestern habe ich dann mehrere Versuche gemacht und zunächst die Original Sony Android Version drauf gespielt und später an /e/ OS.

## Schritt 1: Installation Original Sony Android 9

Es wird immer wieder empfohlen, das originale Android neu zu installieren. Nur wie soll das gehen? Bisher war meine Information dazu, dass das nur unter Windows funktioniert. Und daran scheitert es ja bei mir.

Aber es geht tatsächlich problemlos unter Linux.

### 1. Xperifirm - Download Sony Firmware

Mit dem [Tool Xperifirm](https://xperifirmtool.com/category/tool) kann man auch unter Linux die passende Sony Firmware downloaden.

Zum Starten der Mono-Anwendung führt man folgendes KOmmando aus:

```bash
~/projects/xperia/XperiFirm_v5.6.5> mono XperiFirm-x64.exe
```

Für mein Sony Xperia XA2 hab ich dann die Version `H3113_Customized DE_50.2.A.3.77-R1B`. Xperifirm packt die Firmware bereits im gewählten Unterverzeichnis aus.

### 2. Newsflasher

:::{seealso}
* [Anleitung und Links zu `newsflasher`](https://forum.xda-developers.com/t/tool-newflasher-xperia-command-line-flasher.3619426/)
* [GitHub von `newsflasher`](https://github.com/munjeni/newflasher)
* [Release 52 mit Binaries](https://forum.xda-developers.com/attachments/newflasher_v52-zip.5423079/)
:::

Wichtig: Das `newsflasher` Binary (in meinem Fall `newflasher.x64`) muss in das Firmware-Verzeichnis kopiert werden. `newsflasher` flasht alles, was in seinem aktuellen Verzeichnis liegt.
```bash
~/projects/xperia/H3113_Customized DE_50.2.A.3.77-R1B> sudo ./newflasher.x64
```

### 3. Sony Xperia XA2 Android 9 - wo ist das WLAN?

Nach dem Flashen der Firmware hab ich sie auch mal ausprobiert. Ziemlich schnell war mir wieder klar, dass mir die Original-Firmware nur auf den Wecker geht. Was man alles zusätzlich installieren soll bzw. muss. Das nervt. Sehr skurril war, dass das WLAN nicht funktioniert hat. Ein Neustart hat nichts gebracht. Aber was soll's. Ich wollte dieses Android ja ohnehin nicht einsetzen.

Aber jetzt könnte ich ja nochmal Sailfish probieren. Vielleicht hat sich ja ein Wunder ergeben und die Sony-Firmware hat irgendwas der internen Treiber aktualisiert. Wer weiß.


## Nochmal Sailfish OS 4.4.0 probieren

Also habe ich nochmal Sailfish OS 4.4.0 installiert und habe das Handy einen Tag benutzt. Leider keine Verbesserung. Es bleibt dabei, dass Android-Apps - insbesondere Osmand - einfriert.

## Installation von /e/OS

:::{seealso}
[Installations-Anleitung von /e/OS auf dem Sony Xperia XA2 (pioneer)](https://doc.e.foundation/devices/pioneer/install)
:::

Die [Installations-Anleitung](https://doc.e.foundation/devices/pioneer/install) ist ausführlich und vollständig. Nur im ersten Moment wirkt das kompliziert. Wichtig ist, dass man alle Hinweise liest und beachtet.

Meine Schritte waren wie folgt, da der Bootloader ja bereits entsperrt war.

### 1. Nochmal die Sony-Firmware installieren

Dieses Mal habe ich nach dem Flashen mit newsflasher direkt in den fastboot-Mode gebootet. Vielleicht war das ein Fehler, wie sich später gezeigt hat (s.u.). Ich kann also nicht sagen, ob zu diesem Zeitpunkt WLAN und SIM funktioniert hatten.

### 2. Installation /e/OS


#### Installation des Recovery Programms

```bash
~/projects/xperia/eos> fastboot flash boot recovery-e-0.23-r-20220405175826-dev-pioneer.img                                                                                                                                     ✔
Sending 'boot_a' (22345 KB)                        OKAY [  0.784s]
Writing 'boot_a'                                   OKAY [  0.191s]
Finished. Total time: 0.999s
```

Das geht sehr schnell. Ins Recovery-Programm kommt man nun wie folgt:

* Gerät ausschalten
* `Volume down` (Lautstärke-Button unten) und `Power` drücken und ca. 2-3 Sekunden halten

#### Kopieren der a-Partition nach b

Mit der verlinkten Anwendung soll man den Inhalt der Partition/Slot `a` nach `b` kopieren, da es sonst ggf. zu Problemen kommen kann, wenn die Installation auf `b` zu alt ist. Alles nebulös, aber nachdem der Schritt als verpflichtend marktiert ist, hab ich das durchgeführt.

#### Flashen des /e/OS Image

Ich habe mir das aktuellste Image von R-dev (Android 11) herunergeladen.

```bash
~/projects/xperia/eos> sudo adb sideload e-0.23-r-20220405175826-dev-pioneer.zip
```

Das flashen dauert ca. 4 Minuten. Danach kann man über das Recovery-Menü das Handy neu starten.

### Probleme bei der Installation

Nach der ersten Freude über eine erfolgreiche /e/OS-Installation, hab ich dann ein wesentliches Problem fest gestellt: Die SIM-Karte funktionierte nur teilweise. Zwar wurde der PIN-Code korrekt abgefragt. Aber beim Versuch zu telefonieren kam der Hinweis "Sie müssen den Flugmodus deaktivieren". Nur, der war gar nicht aktiviert.

Also, was nun?

Zunächst habe ich /e/OS Q-dev installiert. Das wäre dann Anroid 10. Dabei hat sich an der SIM-karte aber nichts verbessert.

Ich bin dann wieder zurück gegangen und habe die Sony-Firmware installiert und die Funktionalität dort ausprobiert. Hier hat nun WLAN und SIM funktioniert.
Danach habe ich /e/OS R-dev erneut installiert und jetzt hat auch hier WLAN und SIM funktioniert. Das sind die Probleme, die schwer nachvollziehbar sind.

## Fazit

Ich vermisse die UI von Sailfish-OS, das Email-Programm, den Kalender, den Timer und die gewohnten Wisch-Gesten.

Aber endlich habe ich funktionierendes GPS, Osmand, Streetcomplete und Vespucci laufen klaglos, flüssig und stabil. Alles andere muss ich jetzt lernen.

Mit /e/OS funktionieren nun auch Dinge, die unter Sailfish OS undenkbar wären. So z.B. die [Corona Contact Tracing App](https://codeberg.org/corona-contact-tracing-germany/cwa-android) (ein Fork der Corona Warn App mit Nutzung von microG).

Jetzt bleibe ich erstmal dabei. Und vielleicht komme ich später mal mit dem Sony Xperia III zurück zu Sailfish. Mindestanforderung ist auf jeden Fall ein funktionierendes GPS und eine stabile Android-Virtualisierung.

## Apps

Ein paar Apps, die ich aktuell gerne nutze

| App | Sailfish OS (Android 10)| /e/OS (Android 11) | Store |
|-----|----------|---------|-------|
| [Omand](https://f-droid.org/de/packages/net.osmand.plus/)    |     X     |    X     |   F-Droid    |
| [Streetcomplete](https://f-droid.org/de/packages/de.westnordost.streetcomplete/)    |     X     |    X     |   F-Droid    |
| [Piepmatz](http://werkwolf.com/piepmatz.html)    |     X     |    -     |   Jolla Store / Openrepos    |
| [Vespucci](https://f-droid.org/de/packages/de.blau.android/)    |     -     |    X     |   F-Droid    |
| [Corona Contact Tracing Germany](https://f-droid.org/de/packages/de.corona.tracing/)    |     -     |    X     |   F-Droid    |
| [DB-Navigator](https://www.bahn.de/service/mobile/db-navigator)    |     X     |    X     |   Aurora-Store    |
|     |          |         |       |
