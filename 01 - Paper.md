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

## Données descriptives

Il existe une différence dans la performance des équipes lorsqu'elle joue à domicile ou à l'extérieur (voir [](#home_away)).

:::{figure} ./figures/home_away_effect.png
:name: home_away
Effet sur les résultats des matchs
:::


## Méthode statistiques

**Test T de Student** : Ce test est utilisé lorsque vous comparez les moyennes de deux groupes. Il suppose que les données suivent une distribution normale et que les variances sont égales.

**Test T de Welch** : Ce test est une version modifiée du test T de Student qui ne suppose pas que les variances soient égales.

**Test ANOVA (Analyse de variance)** : Ce test est utilisé lorsque vous comparez les moyennes de plus de deux groupes. Il suppose que les données suivent une distribution normale et que les variances sont égales.

**Test de Kruskal-Wallis** : Ce test est une version non paramétrique de l'ANOVA qui peut être utilisée lorsque les hypothèses de l'ANOVA ne sont pas respectées.

**Test de Mann-Whitney U** : Ce test est une version non paramétrique du test T de Student qui peut être utilisée lorsque les hypothèses du test T de Student ne sont pas respectées.

$\theta = \frac{x}{2}$

:::{table} Table caption
:align: center

| foo | bar |
| --- | --- |
| baz | bim |
:::

## Conclusion

[Fbref]: https://fbref.com/
[WorldFootballR]: https://github.com/JaseZiv/worldfootballR/
[Transfermarkt]: https://www.transfermarkt.com/
