---
tags: linux, jolla, sailfish
date: 2022-04-12
language: de
category: software
---
# Sailfish 4.4.0 auf Sony Xperia XA2 neu flashen

Ich nutze ja schon wirklich lange Jolla bzw. Sailfish OS. Angefangen mit dem Jolla 1 ("First one") Ende 2013 über das Jolla C dann zu Sony Xperia X und seit 2020 das Sony Xperia XA2.

```{figure} my_sailfish_devices.jpg
:alt: fishy
:name:
:class: with-shadow
:width: 600px
:align: center

Meine bisherigen Jolla-Geräte im Jolla-Account

```
Es gibt einige Haken aber das schöne daran ist, man hat ein halbwegs richtiges Linux und kann trotzdem wesentliche Android-Apps nutzen, wie z.B. den DB-Navigator und OsmAnd. Allein die Auswahl der Geräte ist sehr, sehr eingeschränkt und bestimmte Antwendungen, wie z.B. die CoronaWarnApp (CWA) laufen hier nicht. CovPass dagegen schon.

Letzteres machte bei mir Ärger seit SailFish 4.3.0 bei der Nutzung von OsmAnd. Dabei friert die Kartenanzeige ein und die komplette Android Sandbox stürzt ab und startet sich neu. Das ist zum Navigieren super dämlich. Manchmal passiert es sofort, dann wieder erst nach längerer Nutzung.

Heute habe ich mich durchgerungen, das Handy erstmals neu zu flashen. Und zwar mit der Version 4.4.0, die seit ein paar Wochen released ist.

An sich ist das unter Linux kein Problem. Ich habe das ja schon ab und zu gemacht. Aber dieses Mal war mein kleiner Intel NUC doch etwas zickig unter Manjaro Linux mit Kernel 5.15.28. Oder sagen wir mal so, der USB-Port. Das sieht dann folgendermaßen aus:

So:

```bash
bash ./flash.sh
Flash utility v1.2
Detected Linux
Searching device to flash..
Found H3113, serial:CQ3000UJH8, baseband:, bootloader:
Found matching device with serial CQ3000UJH8
Fastboot command: fastboot -s CQ3000UJH8
>> fastboot -s CQ3000UJH8 getvar secure
<< getvar:secure                                      FAILED (remote: 'GetVar Variable Not found')
```

oder auch so:

```bash
bash ./flash.sh
Flash utility v1.2
Detected Linux
Searching device to flash..
Found H3113, serial:CQ3000UJH8, baseband:1311-2845_50.2.A.3.77, bootloader:
Found matching device with serial CQ3000UJH8
Fastboot command: fastboot -s CQ3000UJH8
>> fastboot -s CQ3000UJH8 getvar secure
<< getvar:secure                                      FAILED (remote: 'GetVar Variable Not found')
```

Alles nicht sehr vertrauenswürdig um ein Embedded Device zu flashen. [Der Fehler ist wohl auch bekannt](https://jolla.zendesk.com/hc/en-us/articles/360012031854), es gibt vielfältige Lösungsvorschläge. Genutzt hat keiner davon. Am Ende habe ich das Gerät gewechsel und das Telefon mit einem Thinkpad T470s geflasht. Im ersten Anlauf.

Die Ausgabe vn lspci meines Intel NUCs:

```bash
lspci
00:00.0 Host bridge: Intel Corporation Xeon E3-1200 v5/E3-1500 v5/6th Gen Core Processor Host Bridge/DRAM Registers (rev 08)
00:02.0 VGA compatible controller: Intel Corporation Skylake GT2 [HD Graphics 520] (rev 07)
00:14.0 USB controller: Intel Corporation Sunrise Point-LP USB 3.0 xHCI Controller (rev 21)
00:14.2 Signal processing controller: Intel Corporation Sunrise Point-LP Thermal subsystem (rev 21)
00:16.0 Communication controller: Intel Corporation Sunrise Point-LP CSME HECI #1 (rev 21)
00:17.0 SATA controller: Intel Corporation Sunrise Point-LP SATA Controller [AHCI mode] (rev 21)
00:1c.0 PCI bridge: Intel Corporation Sunrise Point-LP PCI Express Root Port #5 (rev f1)
00:1e.0 Signal processing controller: Intel Corporation Sunrise Point-LP Serial IO UART Controller #0 (rev 21)
00:1e.6 SD Host controller: Intel Corporation Sunrise Point-LP Secure Digital IO Controller (rev 21)
00:1f.0 ISA bridge: Intel Corporation Sunrise Point-LP LPC Controller (rev 21)
00:1f.2 Memory controller: Intel Corporation Sunrise Point-LP PMC (rev 21)
00:1f.3 Audio device: Intel Corporation Sunrise Point-LP HD Audio (rev 21)
00:1f.4 SMBus: Intel Corporation Sunrise Point-LP SMBus (rev 21)
00:1f.6 Ethernet controller: Intel Corporation Ethernet Connection I219-V (rev 21)
01:00.0 Network controller: Intel Corporation Wireless 8260 (rev 3a)
```