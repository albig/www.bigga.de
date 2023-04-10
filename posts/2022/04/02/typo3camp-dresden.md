---
tags: typo3, dresden, t3cmd, barcamp
date: 2022-04-02
language: de
category: software
---

# TYPO3Camp Mitteldeutschland in Dresden

om Do, 31.03.2022 bis Sa, 02.04.2022 war das [4. TYPO3Camp Mitteldeutschland](https://typo3camp-mitteldeutschland.de/) in Dresden. Am Freitag und Samstag war ich dabei und habe mir allerlei Sessions angehört. Hier ein paar Notizen von Themen, die für mich interessant / neu waren.

Eine offizielle Nachlese ist auch verfügbar: [https://typo3camp-mitteldeutschland.de/nachlese](https://typo3camp-mitteldeutschland.de/nachlese)

## codeception PHP Testing

Davon habe ich bisher keine Ahnung und ich habe auch nicht an der Session teilgenommen. Am Ende war es die beliebteste Session des Camps.

[https://docs.typo3.org/m/typo3/reference-coreapi/main/en-us/Testing/WritingAcceptance.html](https://docs.typo3.org/m/typo3/reference-coreapi/main/en-us/Testing/WritingAcceptance.html)

## XIMA Synchronisation als Entwicklungstool

Konrad Michalik von XIMA hat vorgestellt, was er in den letzten zwei Jahren entwickelt hat um die Datenbanken auf Live, Staging und lokalem Entwicklungssystem abgleichen zu können.

Herausgekommen ist das Tool db-sync-tool: [https://github.com/jackd248/db-sync-tool](https://github.com/jackd248/db-sync-tool)

* reine Datenbanksynchronisation
* Anforderung war eine systemunabhängige Unterstütztung für TYPO3, Drupal und Symfonie-Projekte
* Realisierung als Python CLI tool

XIMA setzt es z.B. dafür ein, um den Stand der aktuellen Live-Datenbank in das lokalen DDEV-System der Entwickler zu ziehen.

Auch eine Anbindung an GitLab-CI ist im Einsatz.

Um Dateien zu synchronisieren, nutzt man file-sync-tool was aber nur Wrapper für rsync.

Um lokal fehlende Dateien nachzuladen, wird die Extension [File Fill (`ichhabrecht/filefill`)](https://extensions.typo3.org/extension/filefill) genutzt.

Tipp: PHP Deployer, [https://deployer.org/](https://deployer.org/)


## Dokumentation

Mehrere Sessions drehten sich um das Thema Dokumentation. Ich habe alle besucht, in der Hoffnung mal zu lernen, wie man es richtig macht. Deshalb waren auch alle anderen da. Das war etwas ernüchternd. Antworten gab es keine allumfassende aber ein paar Tipps:

* Für wen schreibe ich die Doku?

* Denkt auch an die Commit-Messages!

* Man kann die TYPO3-Dokumentation auch im MarkDown schreiben.

Tipps:

* Verwendung der TYPO3 [Commit Messages Summary Line](https://docs.typo3.org/m/typo3/guide-contributionworkflow/main/en-us/Appendix/CommitMessage.html#summary-line-first-line).

* Es gibt einen "rst to confluence" Converter ([rst2confluence](https://pypi.org/project/rst2confluence/)). Man kann damit einfach die rST-Dokumentation in Confluence überführen.

* Dokumentation im Backend für Redakteure: Doc-Extension ([`georgringer/doc`](https://github.com/georgringer/doc)) von GeorgRinger

* Extension Helper Benjamin Kott ([`bk2k/extension-helper`](https://github.com/benjaminkott/extension-helper))

## Dokumentation bei Tritum

[Tritum aus Jena](https://www.tritum.de/) dokumentiert seit 2-3 Jahren "alles" (interne Prozesse, Kundendokumentation). Hintergrund ist u.a., dass man nur so eine QM-Zertifikzierung erlangen kann.

Da auch viele Nicht-Techniker dokumentieren, hat man sich dazu entschlossen ein TYPO3-System mit angepassten Bootstrap-Package zu verwenden. Individuelle Kundenzugänge sind auf die Weise für eine TYPO3-Agentur ja auch kein Problem.

Kleines Gimmig am Rande: Auch ein "Signatur-Generator" wurde implementiert. Das ist dann auch für Onboarding der zentrale Anlaufpunkt für neue Mitarbeiter.

Jedes Team nimmt sich jede Woche 1 Stunde Zeit für Dokumentation. Mehr nicht.

## Cookieless Tracking

Die Frage kam auf, ob es mit Matomo möglich ist, Cookieless zu Tracken. Daraus ergab sich eine Session und folgende Erkenntnisse:

* in Matomo gibt es ein Extra-Menü "DSGVO-Übersicht"
* es lassen sich Cookies pro host aber auch global abstellen. Im letzteren Fall wird das matomo.js entsprechend serverseitig angepasst.

Eine junge Alternative ist [https://plausible.io/](https://plausible.io/)

Von Daniel Siepmann gibt es eine [Proofe-of-Concept Tracking-Extension](https://daniel-siepmann.de/projects/typo3-extension-tracking.html), die die Nutzung von Middleware und eine Dashboard-Einbdingung demonstrieren soll. Für einfache Tracking-Aufgaben eventuell ausreichend.

## Tooling

Welche Tools werden im Agentur-Umfeld eingesetzt. Insbesondere für Kommunikation und Projektabrechnung.

In der Diskussion hat sich gezeigt:

* viele setzen selbst gebaute Timetracking-Lösungen ein. Teils will man dabei bleiben. Teils sucht man nach Standardlösungen.
* Focus ist meist Projektzeiten richtig zu erfassen, damit sie abgerechnet werden können. Arbeitszeiterfassung ist eher zweitrangig.
* Mitarbeiter finden kreative Wege, die Zeiterfassung zu umgehen, wenn es nicht gut gemacht ist. Nach 2-3 Tagen wird es immer unschärfer, wenn man Zeiten nachträgt.
* Bei den Kommunikationstools wurde während der Pandemie viel ausprobiert. Die einen sind dann bei Teams, die anderen bei Zoom hängen geblieben. Teils waren so "weiche" Features wie unscharfe Hintergründe das ausschlaggebende Kriterium.
* Es wird eine Verzettelung in den Tools festgestellt. Mehrere Chat-Systeme, Videokonferenz-Systeme ersetzen den Flurfunk. Aber es ist schwierig bis unmöglich Informationen wieder zu finden.

Tools:

* [BCS Projecton](https://www.projektron.de/projektmanagementsoftware/) - kann viel ist aber closed source
* Kimai - Zeit und Projektstunden
* Odoo


## Extensions

Extension, die bei Flurgesprächen immer wieder zur Sprache kamen, die ich mir mal anschauen sollte:

* mask ([`mask/mask`](https://github.com/Gernott/mask))
  *  verified Extension

* container als Alternative für Gridelements ([`b13/container`](https://github.com/b13/container))
  *  verified Extension

* core: opendocs, zeigt zuletzt geöffneten seiten, inhaltselemente

* redirects

reports, xclass-registrierung, solr Konfiguration


TYPO3 11 hat keine PackageStates.php mehr; ext_emconf.php deprecated

siteConfiguration import aus einzelnen Dateien --> SitePackage Builder

## Mask Extension

Der aktuelle Maintainer ([Nikita Hovratov](https://github.com/nhovratov)) sowie der Extension-Owner ([Gernot Ploiner](https://github.com/Gernott)) waren auf dem Camp und haben eine Session zu [mask](https://extensions.typo3.org/extension/mask) gemacht. Ich kannte die Extension bisher nicht.

Mask generiert Code dynamisch, ist eine GUI für TCA. Kein Wartungsaufwand bei TYPO3-Uprades (TCA Änderungen) da Mask seine Config aus dem Json holt.

Normalerweise macht man neue, angepasste Inhaltselemente "zu Fuß": TCA, Tsconfig und Tabellen anlegen.

Mit individuellen Inhaltselementen müssen Redakteure z.B. nicht das Media-Element mit irgendwelchen Verrenkungen lernen.

Seit Mask 6 hat Nikita das Backend Modul durch eine  VueJS-Anwendung ersetzt. Er meint, das alte Extbase/Fluid/jQuery-Modul war nicht mehr wartbar.

Aktuell ist mask für TYPO3 10&11 maintained. Für TYPO3 12 ist es "verified". "verified" bedeutet, dass die Extension vor dem LTS-Release von 12 kompatibel sein wird. Es werden zudem bestimmte Wartungs- und Service-Level zugesichert.

Für Releases nutzt Nikita [Tailor](https://github.com/TYPO3/tailor). Das macht Releases leicht und deshalb erstellt er für jeden Bug-Fix ein neues Patchlevel-Release.

Der Entwicklung kann man auf dem GitHub Project KanBan-Board folgen: https://github.com/Gernott/mask/projects/1

Fazit: Sollte man sich mal anschauen. Eventuell kann man sich bestimmte Konzepte abschauen.

## Code linting, cleanup.

Eine ausführliche Session zu den verschiedenen Möglichkeiten mit Code-Lintern in der Extension-Entwicklung zu arbeiten. [Thomas Kieslich](https://www.thomaskieslich.de/) von Davitec hat sein Setup auf Gitlab veröffentlicht: https://gitlab.com/thomaskieslich/t3cmd22

Inspirit hat er sich u.a. in Oliver Klees [tea-Extension](https://github.com/oliverklee/ext-tea).

```
require-dev {
   helmich/typo3-typoscript-lint
   friendsofphp/php-cs-fixer
   typo3/coding-standards
}
```
Fazit: Müsste man sich mal mit beschäftigen.

Nur eine kurze Notiz. Ich muss mir mal getopts mit bash anschauen.

```bash
while geopts "p:tt:" option; do
   case $option in
   p) ...
done
```
