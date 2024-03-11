---
tags: opensource, wordpress, webdesign, css
date: 2024-03-11
language: de
category: wordpress, software
---

# WordPress-Allerlei für den Löbtop e.V.

Letztes Jahr hatte ich der neuen [Webseite des Löbtop e.V.s](https://loebtop.de) auf die Welt geholfen. In ein paar Tagen [jährt sich der Relaunch](https://loebtop.de/2023/03/22/gemeinsamer-internetauftritt/) und jetzt komme ich endlich dazu, ein paar Details zu korrigieren, die mich schon lange stören.

Die Gestaltung ist von [Lars Uhlmann](https://www.excorporalux.de/), der ja auch sonst schon viele Grafikarbeiten für den Löbtop e.V. und andere lokale Initiativen wie [Willkommen in Löbtau e.V.](https://www.willkommen-in-loebtau.de) gestaltet hat.

Wir hatten damals das aktuelle WordPress-Theme TwentyTwentyThree verwendet und unsere Anpassungen in ein Child-Theme gepackt. Das Child-Theme liegt in [meinem GitHub-Bereich](https://github.com/albig/twentytwentythree-child).

Konkret umgesetzt habe ich jetzt:

1. Die Sichtbarkeit der Webseitensuche
2. Bessere Gestaltung der mobilen Navigation

## Webseiten-Suche

Eine Webseitensuche bringt WordPress ja mit. Man muss nur den Suchschlitz im Theme einbinden und schon funktioniert alles. Soweit so einfach.

Da wir aber im Kopfbereich schon ein Logo, ein Slogan / Tagline, und die Navigation untergebracht haben, funktionierte das mit dem Standard-Block "Search" nicht zufriedenstellend.

Mit ein wenig Basteln habe ich die Suche jetzt aus folgenden Komponenten umgesetzt:

* einem Icon (Suchlupe), wie sie das WordPress-Theme mit bringt
* einem Modal, was das Suchfeld im Vordergrund anzeigt
* einem Overlay, was den Hintergrund hinter dem Modal verschwimmen lässt

Das funktioniert mit einer Kombination aus HTML-Markup im [`header.html`](https://github.com/albig/twentytwentythree-child/blob/main/parts/header.html)-Partial, etwas JavaScript in [`search-modal.js`](https://github.com/albig/twentytwentythree-child/blob/main/assets/js/search-modal.js) und CSS im [`style.css`](https://github.com/albig/twentytwentythree-child/blob/main/style.css).

So sieht das dann aktuell aus:

```{figure} loebtop-suche-2024-03-11_17-34.png
:alt: Screenshot des Such-Schlitz als Modal über einem unscharfen Hintergrund von der Webseite loebtop.de.
:class: with-shadow
:width: 800px
:align: left

Screenshot des Such-Schlitz als Modal auf der Webseite loebtop.de
```

Noch nicht perfekt, aber Welten besser als vorher.

## Inhaltsverzeichnis auf Mobil-Geräten

Der zweite Punkt, der wirklich unschön gelöst ist im TwentyTwentyThree-Theme, ist die "Mobile Navigation". Also das Menü auf kleinen Geräten, wie Smartphones. Dabei werden nämlich nicht die Unterpunkte zusammengeklappt ("collapsed"), es gibt entsprechend keinen "Aufklapp-Pfeil" und die Schriftgröße war auch viel zu klein für Touch-Geräte.

Das Problem ist bekannt und im [GitHub-Issue](https://github.com/WordPress/gutenberg/issues/38599) gibt es auch einen Lösungsvorschlag, den ich dann adaptiert habe.

Hier finden sich die Änderungen im CSS und JavaScript in [`navigation.js`](https://github.com/albig/twentytwentythree-child/blob/main/assets/js/navigation.js)

So sah es bisher aus:

```{figure} loebtop-mobile-navigation-alt-2024-03-11_17-43.png
:alt: Screenshot des Such-Schlitz als Modal über einem unscharfen Hintergrund von der Webseite loebtop.de.
:class: with-shadow
:width: 350px
:align: center

Screenshot des Such-Schlitz als Modal auf der Webseite loebtop.de
```

Und so jetzt:

```{figure} loebtop-mobile-navigation-new-2024-03-11_17-43.png
:alt: Screenshot des Such-Schlitz als Modal über einem unscharfen Hintergrund von der Webseite loebtop.de.
:class: with-shadow
:width: 350px
:align: center

Screenshot des Such-Schlitz als Modal auf der Webseite loebtop.de
```

Auch noch nicht perfekt, aber deutlich einfacher zu handhaben.
