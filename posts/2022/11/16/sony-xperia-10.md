---
tags: linux, jolla, sailfish, eos, sony
date: 2022-11-16
language: de
category: software
---

# Neues, altes Handy - Sony Xperia 10

Mein Sony Xpera XA2 ist am 25.11.2022 zwei Jahre alt geworden. An sich funktioniert es immer noch gut. Bis auf das gelegentlich zickige GPS. Anfangs dache ich ja, es liegt an SailfishOs, aber auch mit /e/OS wurde das nicht besser.


Auf jeden Fall hab ich mir ein neues, altes geleistet und zwar das Sony Xperia 10. Auch schon längst nicht mehr auf dem Markt, aber als fast neues Gebrauchtgerät bei [Smallbug.de](https://smallbug.de) zu ergattern.

Warum das?

1. Es ist halbwegs günstig mit ~181 €.
2. Es lässt sich sowohl [Sailfish OS](https://docs.sailfishos.org/Support/Supported_Devices/) als auch [/e/OS](https://doc.e.foundation/devices/kirin/install) und [LineageOS](https://wiki.lineageos.org/devices/kirin/) installieren.


## Vorgehen

### Unlocking Bootloader

Anleitung von /e/OS: https://doc.e.foundation/devices/kirin/install

1. Unlock code von Sony-Seite abrufen http://developer.sonymobile.com/unlockbootloader/unlock-yourboot-loader/
2. Bootloader entsperren
```bash
~/projects/xperia> fastboot oem unlock 0x8902ACA7D5150903

OKAY [  1.339s]
Finished. Total time: 1.339s
```
:::{hint}
Wenn der Befehl nicht sofort ausgeführt wird, sondern die Ausgabe "hängt" und das Telefon aus dem Fastboot Mode geht, dann sollte man einen anderen USB-Port nutzen.
:::

## Recovery Installieren

```bash
~/projects/xperia/eos> fastboot flash boot recovery-e-1.5.1-s-20221103231515-dev-kirin.img

Sending 'boot_b' (23965 KB)                        OKAY [  0.865s]
Writing 'boot_b'                                   OKAY [  0.173s]
Finished. Total time: 1.080s
```

## Fazit

Läuft gut und ich hatte gleich Android 12 (!) drauf.
