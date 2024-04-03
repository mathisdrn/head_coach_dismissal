---
title: Head coach dismissal effect on football team performance
subject: Statistical analysis
subtitle: Evolve your markdown documents into structured data
short_title: Paper
license: CC-BY-4.0
keywords: coach dismissal, team performance
date: 02/10/2024
---

+++ {"part": "abstract"}

The goals of this paper is to investigate the effect of coach dismissal on team performance. To do that, we will use traditional statistical method that we apply to football teams. 

+++

## Introduction 

Le papier de recherche [](doi:10.3390/economies8040082) sera une référence majeure à ce travail.

Utilisation de la librarie [WorldFootBallR] pour collecter des données sur les sites suivant [Fbref] et [Transfermarkt].

## Le jeu de donnée
- les sites utilisés
- la fiabilité des données
- les données concernés

## Statistiques descriptives
Il existe une différence dans la performance des équipes lorsqu'elle joue à domicile ou à l'extérieur (voir [](#venue_effect)).

:::{figure} ./figures/venue_effect.png
:name: venue_effect
Venue effect on team's performance
:::

- changement des conditions de récupération de donnée [0] https://www.sports-reference.com/bot-traffic.html
- seule donnée disponible : valeur marchande des joueurs
- idée du score de propensité : recréer artificiellement un groupe contrôle et un groupe test

## Conclusion

[Fbref]: https://fbref.com/
[WorldFootballR]: https://github.com/JaseZiv/worldfootballR/
[Transfermarkt]: https://www.transfermarkt.com/
