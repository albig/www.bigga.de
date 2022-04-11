---
tags: linux, coding, spickzettel
date: 2022-04-11
language: de
category: software
---

# Dateien beim Speichern direkt mit externen Server syncronisieren

## Anforderung

Manchmal gibt es Situationen, da möchte man direkt auf einem Ziel-Server arbeiten aber doch gerne die lokale IDE oder den lokaen Editor nutzen.

Ein Weg von vielen, könnte der Zugriff über `sshfs` sein. Also das lokale mounten des entfernten Dateisystems über SSH.

## Inotify-Tools
Noch einfacher ist es mit den inotify-tools. Damit lässt sich das aktuelle Projektverzeichnis sehr simple bei jeder Änderung synchronsisieren.

GitHub-Repo: https://github.com/rvoicilas/inotify-tools

Bei Manjaro und Arch heißt das Paket: `inotify-tools`

Einfaches Skript um die Daten des lokalen Verzeichnisses auf ein Zielverzeichnis zu syncronisieren. Das ganze geschieht rekursiv.

```bash
#!/bin/sh

if [ ! "$1" ]; then
        echo "ERROR: Target parameter is required. E.g. user@example.com:/home/user/target"
        echo "Usage:"
        echo "  notifysync.sh user@example.com:/home/user/target"
        exit 1
fi

# the target of the rsync command. E.g. "user@example.com:/home/user/target"
TARGET=$1

# On every change, inotifywait will exit and the rsync will be executed.
while inotifywait -e modify,create -r ./; do
    rsync -a --delete ./ $TARGET
done
```

Man kann das auch als Einzeiler in der Shell eingeben:
```shell
$> while inotifywait -e modify,create -r ./; do rsync -a --delete ./ user@example.com:/home/user/target; done
```
