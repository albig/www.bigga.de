---
tags: server, hetzner, nextcloud, typo3, wordpress
date: 2023-07-03
language: de
category: technik
---

# Server-Umzug nach 5 Jahren - aus CPX11 wird CAX11

So 5 Tage vor dem Urlaub ist sicher ein guter Zeitpunkt, den privaten Server zu aktualisieren. Und zwar nicht so ein bisschen, sondern von Debian 11 auf 12 mit PHP 7.4 auf 8.2 und dann auch noch die Prozessor-Architekur zu wechseln von Intel x64 auf arm64. Natürlich alles [virtuell in der Hetzner Cloud](https://www.hetzner.com/de/press-release/arm64-cloud). Für meinen Krimskrams brauch ich ja keinen eigenen Server.

Mit der arm64-Architektur bekommt man mehr Leistung zum gleichen oder geringeren Preis. Und die Software? Da [Debian einen vollständigen arm64-Port](https://wiki.debian.org/Arm64Port) hat, kann man alles aus den Debian-Repositories installieren und nutzen. Was anderes brauche ich ja nicht.

## Vorgehen bei Hetzner

Um es mir einfach und zeitlich entkoppelt zu machen, hab ich mir einen neuen Server vom Typ CAX11 (arm64) und Debian 12 angelegt und wie üblich mit Ansible als Webserver vorbereitet.

Danach hab ich nach und nach ein Service nach dem anderen umgezogen.

```{figure} 2023-07-03_19-55.png
:alt: Sreenshot vom Cloud-Backend. Grünes Icon beim neuen Server "liblo" und graues Icon (ausgeschaltet) beim alten Server "dadu", der "vor etwa 5 Jahren" angelegt wurde.
:class: with-shadow
:width: 800px
:align: left

Neuer Server (CAX11) - alter Server (CPX11) bei Hetzner
```

Und weil's so schön war, hab ich mir für ein paar Monitoring-Tools noch einen weiteren CAX11-Server angelegt. Am Ende spare ich jetzt nichts, hab aber dafür zwei virtuelle Server.

## Aktuell genutzte Services / Domains

Konkret läuft auf den Servern:

* [bigga.de](https://bigga.de) - diese Seite / dieser Blog
* [dadu.eu](https://dadu.eu) - die Familien-Cloud [[Nextcloud](https://nextcloud.com/de/)]
* [office.dadu.eu](https://office.dadu.eu) - Collabora Office für die Nextcloud [[Collabora Office Online](https://www.collaboraoffice.com/collabora-online/)]
* [doris-bigga.de](https://doris-bigga.de) - Doris Bigga - Aromatherapie [[TYPO3](https://typo3.org/)]
* [dresden-west.de](https://dresden-west.de) - Dresdner Grüner Westen - Blog [[Wordpress](https://wordpress.org/])
* [gerlinde.bigga.de](https://gerlinde.bigga.de) - Gerlinde Bigga - Blog [[Wordpress](https://wordpress.org/]
* [schwanen-nussbach.de](https://schwanen-nussbach.de) - Gasthaus Schwanen Nussbach [TYPO3](https://typo3.org/)]
* [time.abigga.de](https://time.abigga.de) - Projekt- und Arbeitszeiterfassung [Kimai]
* [liblo.de](https://liblo.de) - Liblo - Reiseblog [[Wordpress](https://wordpress.org/]
* [matomo.abigga.de](https://matomo.abigga.de) - Besuchertracking [Matomo]
* [monitor.abigga.de](https://monitor.abigga.de) - einfaches Server-Monitoring [[PHP Server Montioring](https://www.phpservermonitor.org/)]
* [munin.abigga.de](https://munin.abigga.de) - einfaches Server-Monitoring [[Munin](https://munin-monitoring.org/)]
* [osm.bigga.de](https://osm.bigga.de) - OSM Demo Seite [TYPO3](https://typo3.org/)]
* [weltcafe-dresden.de](https://weltcafe-dresden.de) - alte Weltcafé-Dresden Seite (z.Zt. kaputt) [TYPO3](https://typo3.org/)]
* und noch ein paar Kleinigkeiten.

## Auf die nächsten 5 Jahre!

Wenn alles geklappt hat, kommt auch dieser Blog-Inhalt auf dem neuen Server an. Dann lass ich den Server wieder 5 Jahre laufen. Oder auch nicht. Mal sehn.

Jetzt kommen erst mal die anderen virtuellen Server dran, die ich für [Willkommen in Löbtau e.V.](https://www.willkommen-in-loebtau.de) und (wenige) andere adminstriere.
