---
tags: linux, eos, sony, android
date: 2024-12-25
language: de
category: software
---

# /e/OS Upgrade auf Version 2.6.3 mit Android 14

Nachdem ich [im Mai auf /e/OS Android 13 geupdated habe](/posts/2024/05/23/sony-xperia-10-android-13.md), hab ich mich jetzt auch an das Update auf Android 14 gewagt. Die Schritte hab ich mir ja zum Glück notiert. Und das hat auch hier funktioniert.

## Vorgehen

Anleitung von /e/OS für das Sony Xperia 10: [https://doc.e.foundation/devices/kirin/install](https://doc.e.foundation/devices/kirin/install)

### Download des Images

Download des aktuellen Images für Android U (14) von [https://images.ecloud.global/dev/kirin/](https://images.ecloud.global/dev/kirin/). Aktuell ist das [e-2.6.3-u-20241218455571-community-kirin.zip](https://images.ecloud.global/community/kirin/e-2.6.3-u-20241218455571-community-kirin.zip).

### Recovery Mode aktivieren

1. USB-Debugmode prüfen und ggf. einschalten
2. Handy ausschalten und nicht an USB anschließen
3. Volume-Down und Power lange drücken und loslassen, sobald Gerät startet
4. im Recovery-Menü wählen: Apply Update -> Apply from ADB
5. USB-Verbinden
6. Verbindung testen

```bash
~/projects/eos> sudo adb devices -l
List of devices attached
CQ3001M3VP             sideload usb:1-3.1.2 product:lineage_kirin model:Xperia_10 device:kirin transport_id:1
```

5. Image mit `adb` flashen:

sudo adb devices -l
```bash
~/projects/eos> sudo adb sideload e-2.6.3-u-20241218455571-community-kirin.zip
Total xfer: 1.00x
```

Bei 47% stockte es ein paar wenige Minuten. Einfach warten und dann neu starten.

## Fazit

Änderungen hab ich auf die Schnelle keine feststellen können.

Trotzdem werde ich mir [nach nun 26 Monaten](/posts/2022/11/16/sony-xperia-10.md) bald mal ein neues, gebrauchtes Smartphone suchen müssen. Die Hardware schafft es bald nicht mehr, die Kamera ist ja nun auch nicht toll und 5 G hat das [Sony Xperia 10 von 2019](https://doc.e.foundation/devices/kirin) auch noch nicht.
