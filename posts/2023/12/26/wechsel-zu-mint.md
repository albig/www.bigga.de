---
tags: opensource, linux, desktop
date: 2023-12-08
language: de
category: linux
---

# Linux Distro Wechsel von Manjaro nach Mint

## Mache nie ein Update ohne funtkionierende Spannungsversorgung!

Das muss man mir eigentlich nicht sagen. Hab ich doch lange Embedded Linux gemacht und so manches Telefon geflashed (eigentlich immer erfolgreich). Ich weiß eigentlich, was so alles schief gehen kann während des Update-Prozesses.

Trotzdem hab ich mit meinem Lenovo ThinkPad T470s nebenbei ein Manjaro-Update eingespielt mit neuem Kernel. Ist ja keine Firmware und da habe ich mal nicht dran gedacht, dass der ThinkPad mit seinen zwei Akkus ab und zu den Failover nicht hinbekommt und beim Wechsel von einem auf den anderen Akku plötzlich aus ist.

Und so passierte es. Laptop aus. Laptop wieder eingeschaltet und keinen Kernel mehr gefunden. Da war wirklich nix mehr da in `/boot`, auch kein Fallback-Kernel. Ich meine, das macht Manjaro immer so.

Kernel und Initramfs hab ich wieder hin bekommen. Ich konnte auch wieder auf meine LUKS-verschlüsselte Partition zugreifen. Trotzdem war das System ziemlich korrupt, einige Libs lagen als "0-Byte" Dateien rum. Das alles wieder zu reparieren war mir dann zu mühsam. Zudem war das System vor 2 Jahren aufgesetzt worden und eine Neu-Installation wäre auch nicht übel. Damit wollte ich dann auch KDE wieder loswerden. Das sieht zwar hübsch aus, aber ist mir zu oft zu klicky. Ich brauch halt nur meine Terminals und Browser-Tabs.

## Kurzer Ausflug Manjaro XFCE

Also hab ich mir Manjaro in der Variante XFCE heruntergeladen und hab es installiert. Sieht eher altbacken aus, aber das wäre mir ja egal gewesen. Aber dann fiel mir wieder ein, warum ich das vor 2 Jahren nicht genommen habe. Der ganze Workflow mit Laptop an Docking-Station anschließen und wieder trennen klappt zur mäßig. Der Desktop schaltet dann den Laptop-Bildschirm nicht ab, der Sperrbildschirm wird nicht aktiv und selbst das Touchpad war noch nicht mal auf "klick" konfiguriert.

Also dann doch lassen. GNOME? Nee, keine Lust.

## Es geht viel mit Linux Mint

Also hab ich mich daran erinnert, dass Kolleg\*innen Linux Mint empfohlen haben. Hatte ich auch vor Jahren ausprobiert, aber dann wieder verworfen.

Probiert, der Dock-Workflow klappt wunderbar, das Touchpad ebenso und für LUNKS gibt es sogar ein freundliches Eingabefeld für die Festplattenverschlüsselung.

### DDEV, Docker mit Linux Mint

Bei der Festplattenverschlüsselung musste ich LVM oder ZFS auswählen. Warum auch immer, gibt es nicht die Möglichkeit im Installer einfach ohne beides die Festplatte zu verschlüsseln. Ich hab mich für ZFS entschieden. Davon hatte ich bisher wenig Ahnung und man kann ja was dazu lernen.

Das hat alles soweit gepasst, bis ich DDEV und Docker installiert habe. Das lief soweit gut, bis zum ersten Test-Projekt. Das startet nämlich so:

```
Building project images... 
Project images built in 5s. 
 Container ddev-ddev-neu-web  Created 
 Container ddev-ddev-neu-db  Created 
 Container ddev-ddev-neu-web  Started 
 Container ddev-ddev-neu-db  Started 
Waiting for web/db containers to become ready: [web db] 
Failed waiting for web/db containers to become ready: web container failed: log=, err=health check timed out after 2m0s: labels map[com.ddev.site-name:ddev-neu com.docker.compose.service:web] timed out without becoming healthy, status= 
Starting ddev-router if necessary... 
 Container ddev-router  Created 
 Container ddev-router  Started 
Waiting for additional project containers to become ready... 
Failed to start ddev-neu: container(s) failed to become healthy before their configured timeout or in 120 seconds. This might be a problem with the healthcheck and not a functional problem. (health check timed out: labels map[com.ddev.site-name:ddev-neu] timed out without becoming healthy, status=, detail= ddev-ddev-neu-web:starting - more info with `docker inspect --format "{{json .State.Health }}" ddev-ddev-neu-web` ) 

```

Das war für mich sehr überraschend, weil ich mit DDEV nie Probleme hatte. Nach einigem Suchen, hab ich Hinweise gefunden, dass andere Menschen mit ZFS und Docker die selben Probleme hatten. Also hab ich `/var/lib/docker` mal versuchsweise auf eine EXT4-Partition verschoben und siehe da... es funktioniert.

Verrückt. So, jetzt werde ich als Mint noch mal neu installieren mit LVM und EXT4.
