---
tags: linux, clt2023
date: 2023-03-12
language: de
category: software, job
---

# Mein erster Besuch auf den Chemnitzer Linuxtage

Bekannt sind mir die [Chemnitzer Linuxtage](https://chemnitzer.linux-tage.de/) seit meinem Studium. Kein Wunder, es gibt sie ja seit 1999. Da war ich aber nie, weil es zeitlich nie gepasst hast. Obwohl ich ja nur 1:24h Zugminuten (Dresden-Plauen - Chemnitz Süd (direkt)) entfernt wohne.

Ich denke, in Zukunft werde ich öfter kommen. Für den symbolischen Eintrittspreis von 12 € bekommt man zwei Tage viel Input aus dem Bereich Linux, Open-Source, Basteln und Unternehmertum.

## Besuchte Vorträge

Im folgenden meine Notizen zu den Sessions, die ich besucht habe. So hatte ich es ja auch mit dem [TYPO3 Camp Mitteldeutschland 2022](/posts/2022/04/02/typo3camp-dresden/) gehalten.

Die Vorträge sind alle (?) im Stream nachschaubar unter folgender Adresse aufgelistet: [https://streaming.media.ccc.de/clt23/relive
](https://streaming.media.ccc.de/clt23/relive).

### Mach es einfach: Nutze Vim!

* [Programm-Link](https://chemnitzer.linux-tage.de/2023/de/programm/beitrag/102)
* Ein Vortrag von Marie Mann von [Pengutronix](https://www.pengutronix.de/de/)
* [Handout / CheatSheet](https://chemnitzer.linux-tage.de/2020/media/programm/material/222.pdf)

Dinge, die ich bisher nicht drauf hatte:

* Navigation mit den Tasten `h` `j` `k` und `l`. Praktisch nutz ich dann doch immer die Pfeiltasten.
* `:set relativenumber`: Anzeige der relativen Zeilennummern. Das muss ich ausprobieren!
* `dw` für das nächste Wort löschen
* `4dw` entsprechend die nächsten vier Wörter löschen
* Am Ende vom Block einfügen (z.B. bei Listen mit unterschiedlichen Zeilenlängen):
    * `CTRL v` - Bereich im visual Mode markieren
    * `$` - ans Zeilenende springen
    * `A` - am Ende einfügen
    * `ESC`

Letzteres klingt nach einer Lapalie, aber bei manchen Listen bin ich schon daran gescheitert und hab mir dann was anderes überlegt. Einfügen oder Änderungen am Block-Anfang hatte ich drauf.

Des weiteren schau ich mir nochmal an, wie ich mehrere Dokumente öffne - entweder mit split oder als eigener Tab.

Ich muss zugeben, dass ich nie Lust hatte vim systematisch zu lernen. Ich merke mir ein paar Kniffe nach und nach und wende die halt an, bis sie in die Fingerautomatik übernommen sind. Wie das Schreibmaschine schreiben.

### Bildungssysteme nachhaltig digitalisieren

* [Programm-Link](https://chemnitzer.linux-tage.de/2023/de/programm/beitrag/244)

Drei Lehrer aus Baden-Württemberg erzählen aus dem Nähkästchen, wie sie sich schon länger für die Schul-IT engagieren. Im speziellen geht es dann um das Engagement während der Lock-Downs.

In Stichpunkten:
* man hat eine sehr große BigBlueButton Infrastruktur aufgebaut. Nach eigenen Aussagen, eine der größten Installationen weltweit mit zeitweise bis zu 180.000 simultanen Nutzern.
* ca. 28 Instanzen pro Server mit 32 Kernen unter Nutzung von [systemd-nspawn](https://wiki.debian.org/nspawn).
* zunächst 40 Hosts mit 1000 BigBlueButton Instanzen
* Scalelite Server zum Load Balancing
* Kombination von Moodle mit BBB
* in dieser Ausbaustufe hatte man bis zu 30.000 simultane Nutzer

Später wurde alles um den Faktor 10 hochskaliert. Dann waren bis zu 180.000 simultane Nutzer möglich bzw. wurden beobachtet. Server wurden bei Hetzner angemietet. Teilweise musste man auf weniger Leistungsfähigere Geräte setzen, da nichts besseres verfügbar war.

In Baden-Württemberg gibt es bisher keine Schul-Cloud für alle. Für Lehrer wird das jetzt auf Basis der [dPhoenixSuite](https://www.dphoenixsuite.de/) eingeführt. Eine Lösung für alle Schulen wird durch die dezentrale Zustänidgkeit für Schulen verkompliziert.

Aktuell nutzen Schüler*innen sehr viel Google-Mail, weil sie das auf ihrem Android-Handy sowieso haben. Ansonsten ist die gesamte Bandbreite der großen, internationalen Mail-Hoster dabei. Datenschutz spielt hier leider eine geringe Rolle.

In Bayern gibt es wohl mittlerweile eine Schul-Cloud auf Basis von Nextcloud, Onlyoffice und Matrix - sowohl für Lehrer als auch Schüler.

### Digital souveräne Videokonferenzen in Thüringen (OpenTalk)

* [Programm-Link](https://chemnitzer.linux-tage.de/2023/de/programm/beitrag/271)

Der Vortrag war zwei geteilt. Zuerst stellt Christian Stötzer vom Thüringer Finanzministerium die Anforderungen des Landes an eine Video-Konferenzlösung dar.

Anschließend beschreibt Peer Heinlein von Heinlein Support / [OpenTalk](https://opentalk.eu/) die Umsetzung der Anforderungen und die Entwicklung von OpenTalk.

#### Anforderung Land Thüringen

Der Betrieb muss im Landesrechenzentrum Erfurt erfolgen. Man kennt sich schon aus mit

* Osims
* Ceph
* Ansible
* Kubernetes
* Nextcloud seit 2016
* Nextcloud-Talk ab 2019

**Datenschutz, Sicherheit, Souveränität**

Weitere Anforderungen:
* Betrieb im eigenen Rechenzentrum
* skalierbar
* unterschiedliche Sicherheitszonen (intern / extern)
* ende-zu-ende Verschlüsselung
* Anpassung der Videoqualität BB-Management
* IDP  / Keycloak
* Alles aus dem Browser
* Einwahl per Telefon mit Hand heben und Stumm schalten
* Umfragen
* Abstimmung (geheim / öffentlich) mit Protokollierung
* Whiteboard
* Teilnehmer ein / ausschließen
* Herstellung von Öffentlichkeit
* Aufzeichnung von Sitzungen mit Einzel-Opt-in- Funktion
* Screensharing auf ausgelagerten Monitor
* Flüstertaste
* Integration von Email-Client
* Kalendereinladungen werden verschickt
* Zertifizierbarkeit
* Barrierefreiheit

Aktuell laufen Tests mit 250 Nutzern. Ziel sind 4000 Nutzer.

Insgesamt ist das Feedback durchweg positiv.

Eine Zulassung nach VSA ist zur Zeit nicht geplant.

Thüringen ist offen, aber bisher gibt es keine Zusammenarbeit.

Grober Zeitplan: Ab 01.04.2023 soll der erweiterte Probebetrieb starten und ab ca. 01.07.2023 der Produktivbetrieb.

#### Peer Heinlein

Thüringen ist weit vorn und konsequent OpenSource.

Was braucht eine Videokonferenz heute in Politik und Bildung?

BBB und Jitsi funktionieren grundsätzlich und sind OpenSource. Jitsi wird auch bei Mailbox.org eingesetzt.

Aber diese Software-Lösungen sind "alte Veteranen" mit veraltete Architektur. "Irgendwann kann man mit Renovieren nichts mehr reparieren."

Die Videokonferenz Plattform für Berlin auf Basis von Nextcloud Talk realisiert. Aber auch das stößt an seine Grenzen.

Also fiel die Entscheidung, alles von Scratch von vorne zu entwerfen

Videokonferenz neu und zu Ende gedacht.

Kindgerecht

* on premis
* Skalierung
* OpenSource
* Schnittstellen
* Integration

OpenTalk Usecases

* Schulen und Universitäten
* Politik & Behörden
* Podiumsdiskussion
* Usermanagement nach Teams / Fraktionen - Breakouträume
* Unternehmen / NGOs
* Provider / Plattform

Anforderungen:

* Rust, sicher
* Kubernates
* APIs
* Accounting,Abrechnung
* Theming


Features

* Subraumaudio
* Abstimmungen (wer darf abstimmen)


Entwicklung 2 Jahre, anfangs viel Frontend-Entwürfe und keine Programmierung. Mittlerweile ist die Software stabil und man implementiert dieses Jahr noch viele Features.

Parameter zur Laufzeit ändern.

Authentifizierung Keycloak

Controller prüft Zugang, vermittelt an die Ingress-Server.

Ingressserver managed Konferenz. Jede Konferenz ist ein Docker-Container.

Mit Container gehen Logfiles verloren, wenn sie nicht gerettet wird. Positives Feedback.

3 Video streams + 1 Audio.

Rabbit MQ

Ausprobieren kann man OpenTalk unter https://demo.opentalk.eu

Handcharts

Kubernates Enterprise Feature werden kostenpflichtig sein, da mit dem Produkt auch etwas Geld verdient werden muss.

### Wie hört man heute Radio?

* [Programm-Link](https://chemnitzer.linux-tage.de/2023/de/programm/beitrag/128)


### Linux auf den Innenanzeigern der ICE-Flotte der DB

Linux4ICE

* [Programm-Link](https://chemnitzer.linux-tage.de/2023/de/programm/beitrag/121)

DB-Systel GmbH

Andreas Ufert Bayreuth
Markus Müller
Standort Frankfurt, Erfurt, Berlin, Homeoffice

Innen-Anzeiger ICE

Browser Chromium
Über IP individualisiert.

6 verschiedene Intel-Platformen

Yocto

[RAUC](https://github.com/rauc/rauc) für OTA-Updates

### Zur Herausforderung, Unternehmen mit OpenSource aufzubauen

* [Programm-Link](https://chemnitzer.linux-tage.de/2023/de/programm/beitrag/243)

Kivitendo
Dolyvar

### Warum man nicht in der IT arbeiten sollte und warum wir es trotzdem tun

* [Programm-Link](https://chemnitzer.linux-tage.de/2023/de/programm/beitrag/156)


### Vereinsverwaltung mit CiviCRM

* [Programm-Link](https://chemnitzer.linux-tage.de/2023/de/programm/beitrag/238)

Faker Kontakte importieren

Bevorzugt Drupal

### Kunden als Maintainer gewinnen – geht das überhaupt?

Open Culturas

* [Programm-Link](https://chemnitzer.linux-tage.de/2023/de/programm/beitrag/245)

[OpenCulturas](https://openculturas.org)

Agentur [cowain](https://cowain.eu)

Technische Basis ist Drupal.

Verein gegründet

### Infrastruktur als Commons. Wir holen uns das Netz zurück!

* [Programm-Link](https://chemnitzer.linux-tage.de/2023/de/programm/beitrag/183)

www.sudelbuch.de seit 1998

Hostsharing EG

Jeder MA ist Mitglied in der eG
