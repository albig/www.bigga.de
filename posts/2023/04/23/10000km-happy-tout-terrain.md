---
tags: fahrrad, tout-terrain
date: 2023-04-23
language: de
category: fahrrad
---


<link href="/_static/c3.css" rel="stylesheet" />
<script src="/_static/d3.5.min.js" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
<script src="/_static/c3.min.js" crossorigin="anonymous" referrerpolicy="no-referrer"></script>

<script>

var chart = c3.generate({
    size: {
        width: 700,
        height: 500
    },
    data: {
        x: 'date',
        url: '/_static/Rad2023.csv',
        type: 'line',
        types: {
            Tageskilometer: 'bar'
        },
        xFormat: '%d.%m.%Y',
        axes: {
            Kilometerstand: 'y',
            Tageskilometer: 'y2'
        }
    },
    color: {
        pattern: ['#047637', '#6b7ff3', '#B73540', '#B73540']
    },
    axis: {
        x: {
            type: 'timeseries',
            tick: {
                format: '%d. %b %Y',
                rotate: 35,
                count: 36
            }
        },
        y2: {
            show: true,
            label: '[km/d]'
        }
    },
    bar: {
        width: {
            ratio: 0.4
        }
    },
    point: {
        r: 4
    },
    zoom: {
        enabled: true,
        rescale: true
    }
});

</script>

# Happy 10.000 km Tout Terrain!

## Tout Terrain seit 2019
Am 23.04.2023 hat mein [Tout-Terrain](https://tout-terrain.de/) Fahrrad seinen 10.000 km geschafft. Und es läuft wie am ersten Tag.

```{figure} tout-terrain-2023.jpg
:alt: Orangenes Fahrrad steht angeschlossen an einem Fahrradbügel in der Sonne
:class: with-shadow
:width: 400px
:align: left

Mein Fahrrad ist am Fahrradbügel angeschlossen.
```

Gekauft hab ich es Ende 2019 bei [Meißner-Raeder](https://meissner-raeder.de/) in der Dresdner Neustadt. Dabei sind ein Teil meiner Komponenten (Rohloff-Narbe, Sattel, Mäntel) vom Vorgänger übernommen und eingebaut worden. D.h. von Tout-Terrain ist "nur" der Silkroad-Rahmen. Die ganze andere Arbeit hat [Meißner-Raeder](https://meissner-raeder.de/) erledigt. Das hat ein paar Wochen gedauert, da auch die Rohloff-Schaltung eingeschickt werden musste um sie auf Scheibenbremse umzubauen.

Mein Vorgänger war übrigens ein [Rotor-Komet](https://www.rotorbikes.com/). Leider war hier nach 15 Jahren (2004-2019) der Rahmen stark verrostet. Ein Glück, dass ich mich Ende 2019 für ein neues Rad entschieden habe. Ein halbes Jahr später gab es dann ja an allen Ecken Schwierigkeiten mit der Verfügbarkeite von Fahrrad-Teilen.

Seit April 2021 haben wir mit dem  [Rad\*Stadt\*Laden](https://radstadtladen.de/) einen tollen Fahrrad-Laden in Löbtau.Hier lass ich nun die jährliche Wartung (Durchsicht + Ölwechsel bei der Rohloff) durchführen.

Die meisten Kilometer fahre ich im Stadtverkehr, zur Arbeit ([bis Juli 2022](https://www.bigga.de/posts/2022/06/30/10-8-jahre-slub/)) und zur Kita. Ein paar größere Touren konnte ich 2020 von [Rügen nach Bad Muskau](https://liblo.de/2020/06/07/radtour-ruegen-bad-muskau/), 2021 ein paar Tagestouren durch Sachsen und dann 2022 von [Binz nach Köthen](https://liblo.de/2022/06/27/radtour-binz-koethen-2022/).

<div id="chart"></div>

:::{hint}
Die Daten aus dem Chart sind manuell erfasst. Jeden Tag notiere ich mir die Gesamtkilometer. Bisher hab ich keinen fancy Fahrrad-GPS-Computer.

Am Ende habe ich dann eine [einfache CSV-Datei](/_static/Rad2023.csv). Die wird auf der Webseite mit [D3.js](https://d3js.org/) und [C3.js](https://c3js.org/) visualisiert. Kann man bestimmt schöner machen, aber so ging es relativ schnell.
:::

## Vorgänger

Das Tout Terrain hat in Summe ca. 3400 € gekostet. Dabei habe ich die Rohloff-Narbe (von 2010), den Brooks-Sattel (von 2004) und die Mäntel übernommen. Bei letzteren wurde mir empfohlen, sie bald mal zu tauschen. Na, jetzt nach weiteren 10.000km werde ich das im Herbst/Winter auch mal tun. Komplett hätte es also ca. 4500 € gekostet.

Der Vorgänger Rotor Komet hatte in der Anschaffung 2004 knapp 2000 € gekostet und hat gut 15 Jahre gehalten.

Davor bin ich ein einfaches Winora mit 5-Gang-Nabenschaltung gefahren von ca. 1993 bis 2004 - also 11 Jahre. Neupreis ca. 800 DM.
