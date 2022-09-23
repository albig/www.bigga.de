---
tags: linux, mailserver
date: 2022-09-19
language: de
category: software
---

# Update nach 2 Jahren - eigener Mailserver mit Postfix, Dovecot u.a.

Fast genau zwei Jahre betreibe ich meinen eigenen Mailserver für [bigga.de](https://www.bigga.de) und ein paar weiterer Domains. Für den Verein [Willkommen in Löbtau e.V.](https://www.willkommen-in-loebtau.de) mache ich das sogar schon länger - ca. vier Jahre.

Am Anfang bin ich den tollen [Anleitungen von Thomas Leister](https://thomas-leister.de/mailserver-debian-buster/) gefolgt. Ohne die wäre der Einstieg doch schwierig geworden. Denn die Komplexität hab ich doch zunächst unterschätzt.

Wenn's aber läuft, macht das auch Spaß. Und das alleine ist ja auch der Grund, warum sich das für mich lohnt.

## Update von Debian 10 auf 11

Debian 11 ist zwar nicht mehr ganz neu auf dem Markt. Die Webserver hatte ich schnell aktualisiert. Da war es ja im Wesentlichen PHP 7.3 auf 7.4, was weitgehend unkritisch war.

An die Mailserver hab ich mich lange nicht getraut. Entsprechend hab ich erst eine Testumgebung aufgebaut mit einer eigenen Domain und habe meine Ansible-Skripte Stück für Stück angepasst.

An sich sind es keine großen Versionssprünge. Die Änderungen an den entsprechenden Konfigurationen hielt sich deshalb auch in Grenzen. Am sichtbarsten ist das Update bei Roundcube. Das Webmail-Backend ist plötzlich ganz schick geworden.

| Programm | Debian 10 (buster) | Debian 11 (bullseye) |
|-----|----------|---------|
| Postfix | 3.4.23 | 3.5.13 |
| Dovecot | 2.3.4 | 2.3.13 |
| MariaDB | 10.3.36 | 10.5.15 |
| Roundcube | 3.17 | 4.13 |
| Sympa | 6.2.40 | 6.2.60 |

## Neu dabei: Postfixadmin

Bisher hatte ich alle Mail-Konten per Hand in der Datenbank angelegt. Das Datenbank-Schema ist schon sehr übersichtlich, aber cooler wäre es halt, das über eine Oberfläche machen zu können. Das was im Umfeld von Thomas Leisters Anleitung entstanden ist, hat mich nicht so überzeugt.

[Postfixadmin](https://github.com/postfixadmin/postfixadmin) scheint verbreiteter, wird gepflegt und das anzubieten, was ich wollte. Allerdings ist die UI auch irgendwie nicht gerade fertig oder up-to-date. Trotzdem hab ich nun mein Datenbank-Schema darauf umgestellt und Postfixadmin installiert.

## Zertifikate jetzt mit acme.sh

Mit den Arbeiten am Mailserver verbunden war auch der Umstieg von Let'sencrypt Certbot auf [acme.sh](https://github.com/acmesh-official/acme.sh). Jetzt triggere ich für jedes Projekt ein eigenes Zertifikat per Ansible und habe vor allem die vHosts vollständig unter Kontrolle.
