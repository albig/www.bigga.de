---
tags: mp3, ogg,
date: 2022-05-04
language: de
category: technik
---

# MP3-Player - zurück auf Los. Ich schick das Ding zurück.

Nachdem ich [kürzlich viel Zeit in die Recherche](/posts/2022/04/27/mp3player-difficulties.md) nach einem neuen MP3-Player gesteckt habe, erkläre ich das Projekt jetzt für gescheitert. Ich habe die Player zurückgeschickt.

## Linux-Unterstützung mangelhaft

Der "SanDisk Clip Sport Plus" ist ein reines [Mass Storage Device (MSC)](https://en.wikipedia.org/wiki/USB_mass_storage_device_class). D.h. es sollte keine Probleme mit Linux geben, was es bei [MTP (Media Transfer Protocol)](https://en.wikipedia.org/wiki/Media_Transfer_Protocol)-Geräten ja schon manchmal gibt.

Sollte. :-(

Der Player hat ein recht seltsames Verhalten. Verbindet man ihn per USB, erscheint er nicht in der Dateiverwaltung. Sobald man sich aber die Partitions-Tabellen mit `fdisk`, `cfdisk` oder `gparted` anschaut, ist er plötzlich da.

Bitte, was soll das?

Wie so oft - ich war nicht der erste User mit dem Problem. Ich habe meinen Output beim [Bugreport von Archlinux](https://bbs.archlinux.org/viewtopic.php?pid=2034108#p2034108) ergänzt. Das scheint aber kein Arch-Problem zu sein. Es passiert bei Ubuntu ebenso.

Ich vermute ja, es liegt an der seltsamen Partitionierung. Folgendes zeigt mir `fdisk`:

```
Festplatte /dev/sdb: 29,72 GiB, 31914983424 Bytes, 62333952 Sektoren
Festplattenmodell: Clip Sport Plus
Einheiten: Sektoren von 1 * 512 = 512 Bytes
Sektorgröße (logisch/physikalisch): 512 Bytes / 512 Bytes
E/A-Größe (minimal/optimal): 512 Bytes / 512 Bytes
Festplattenbezeichnungstyp: dos
Festplattenbezeichner: 0x2ed3519d

Gerät      Boot Anfang     Ende Sektoren Größe Kn Typ
/dev/sdb1  *    452608 62333951 61881344 29,5G  b W95 FAT32
/dev/sdb2         2048   452607   450560  220M  b W95 FAT32

Partitionstabelleneinträge sind nicht in Festplatten-Reihenfolge.
```

Für was bitte sind die 200M _vor_ der eigentlich nutzbaren Partition?

## Bluetooth-Ton leise

Ja, die Ohren müssen geschützt werden. Über Bluetooth ist der Player aber so leise, dass man zwangsläufig über die Lautstärkebegrenzung gehen muss. Und selbst beim absoluten Maximum ist das nicht wirklich laut. Was soll das? Die Lautstärke wird doch auch nur ein Wert sein, der über Bluetooth übertragen wird, oder liege ich da falsch?

## Umtausch mit Amazon

Ich bestelle ja ausgesprochen selten bei Amazon. I.d.R. findet man alles auch in anderen Shops. Bei diesen MP3-Playern war es anders. So habe ich auch keine Erfahrung mit Retouren zu Amazon. Der Online-Prozess war sehr simpel. Nun reist das Päckchen zurück. Mal sehn, wann das Geld erstattet wird.

## Fazit

Ich lass es erstmal.

Für die Kinder tut's der [Trekstor Move Bt](https://www.trekstor.de/produkte/mp3-player/detail-mp3-player/product/move-bt.html).

Das Problem mit den völlig ungeordneten Hörspielen liegt offenbar an den ID3-Tags. Wenn man die komplett rauslöscht, beachtet er die Dateinamen und darüber kann man - wie "früher" - die Reihenfolge steuern.

Sind die ID3-Tags allerdings drin (was ja sinnvoller wäre), kommen komische Sachen raus.