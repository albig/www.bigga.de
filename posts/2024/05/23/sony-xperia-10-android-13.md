---
tags: linux, eos, sony, android
date: 2024-05-23
language: de
category: software
---

# /e/OS Upgrade auf Version 2.0 mit Android 13

Bald begleitet mich mein [Sony Xperia 10 mit /e/OS](/posts/2022/11/16/sony-xperia-10.md) zwei Jahre. Jeden Monat gab es ein Update. Seit es ein Release "T" - mit Android 13 - gibt, bekomme ich aber keine Updates mehr.

Also musste ich mal wieder das Handy flashen. Hatte darauf jetzt schon ein paar Monate keine Lust, weil ja immer das Risiko bleibt, dass die Daten weg sind oder im schlimmsten Fall das Handy schrottet.


## Vorgehen

Anleitung von /e/OS: [https://doc.e.foundation/devices/kirin/install](https://doc.e.foundation/devices/kirin/install)

### Download des Images

Download des aktuellen Images für Android T (13) von [https://images.ecloud.global/dev/kirin/](https://images.ecloud.global/dev/kirin/). In meinem Fall war das [e-2.0-t-20240508399779-dev-kirin.zip](https://images.ecloud.global/dev/kirin/e-2.0-t-20240508399779-dev-kirin.zip).

### Recovery Mode aktivieren

1. USB-Debugmode prüfen und ggf. einschalten
2. Handy ausschalten und nicht an USB anschließen
3. Power-Down und Power lange drücken
4. im Recovery-Menü wählen: Apply Update -> Apply from ADB
5. Image mit `adb` flashen:


```bash
~/projects/eos> adb sideload e-2.0-t-20240508399779-dev-kirin.zip
Total xfer: 1.00x
```

## Fazit

Auf den ersten Blick, sieht manches anders aus, die Daten und selbst die Hintergrund-Bilder sind erhalten geblieben.

Aber es scheint einen ticken langsamer in der Bedienung zu sein. Tja, das klassische Konzept - mach die Software langsam, dann kaufen Menschen neue Geräte.
