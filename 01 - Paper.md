---
title: Head coach dismissal effect on football team performance
subject: Statistical analysis
subtitle: Evolve your markdown documents into structured data
short_title: Paper
license: CC-BY-4.0
keywords: coach dismissal, team performance
date: 02/10/2024
exports:
  - format: typst
    template: lapreprint-typst
    output: exports/TER_head_coach_dismissal.pdf
    articles:
        - file: 01 - Paper.md
        - file: 02 - Data extraction.ipynb
        - file: 03 - Preprocessing.ipynb
        - file: 04 - Headcoach analysis.ipynb
        - file: 05 - Match results analysis.ipynb
        - file: 06 - Extending EDA.ipynb
        - file: 07 - More preprocessing.ipynb
        - file: 08 - Statistical analysis.ipynb
        - file: 09 - Conclusion.md
---

+++ {"part": "abstract"}
The goals of this paper is to investigate the effect of coach dismissal on team performance. To do that, we will use traditional statistical method that we apply to football teams. 
J'ajoute une ligne
+++

## Introduction 

Sujet du TER : Comprendre l'effet du changement de club sur les performances du coach 
ET NON, comme le sujet initial ([](doi:10.3390/economies8040082)) Comprendre l'effet du changement de coach sur les performances du club
Idée du prof : toutes choses étant égales par ailleurs (ceteris paribus) (idée d'un club représentatif), quelles sont les variations de performances d'un coach au cours du temps et lorsqu'il change de club

Impossible de créer "ce club égal par ailleurs" :

La création d'un club égal par ailleurs nécessite l'intervention d'un modèle qui permettrait, à partir des données du club (masse salariale, budget, performance passé du club, etc.) de normaliser la performance du club afin d'étudier précisemment l'impact du coach sur cette performance 

Ceci pose plusieurs problèmes :
    1. Les variations de performances du coach sont difficilement observable au travers la performance de l'équipe (détailler)
    2. Impossible de respecter l'hypothèse d'uncounfoundness requise par de nombreux modèles statistiques corrigeant les externalités (ex: propensity score / PSM) (citer papier propensity score + expliquer l'idée du propensity score pour artificiellement recréer un groupe contrôle et test artificiel, expliquer l'hypothèse d'uncounfoundness et pourquoi elle est nécessaire)
    3. Biais de causalité (point le plus important !) : on suppose que c'est la performance du coach qui fait varier la performance de l'équipe or, dès lors que cette causalité n'est plus vérifiée on se mord la queue dans la création du modèle explicatif :
    Supposons que ce soit la performance de l'équipe qui causent les variations de performance du coach. Le modèle explicatif, censé créer ce club égale par ailleurs, va être amené à normaliser plus fortement un club qui performe bien par le passé. Or si c'est la performance de l'équipe qui cause la performance du coach on est en train de normaliser les variations de performance du coach. (mentionner l'existence de test d'inversion de la causalité + référence au papier) (expliquer ce que sont les fuites de données (data leakage) et que l'absence de cette hypothèse de causalité provoque des fuites de données entre les externalités et la variable d'interêt (la performance du coach)).
    4. Le peu de donnée (retrouver le chiffre sur le nombre de club avec au moins 2 ou 3 changements de coach) (expliquer que dans la problématique initiale il y a bien plus de donnée car il y a davantage de club qui ont vu passer de coachs que de parcours individuel de coach au sein de clubs)
    5. Problème de temporalité : les données sur les budgets des équipes, masse salariale ou valeur marchande des équipes ne sont pas disponible sous forme temporelle : impossible de savoir si la hausse de performance de l'équipe est dûe à la hausse du budget de l'équipe ou inversement.
    6. Faible qualité des variables exogènes permettant l'analyse du système : 
        - Manque " d'objectivabilité " des variables externes : masse salariale (pas représentative, ex : sous-traitance), valeur marchande des joueurs (hautement subjectif)
        - Manque de diversité des variables  

Conclusion :
Lors de l'analyse des effets dans un système, on raisonne généralement à petite entité égales par ailleurs
Exemple :  On parle d'agent économique représentatif et rarement d'une économie représentative :
- On observe l'effet de l'économie sur un agent économique 
- et NON l'effet d'un agent économique sur l'économie
(à nuancer pour ne pas déplaire aux micro-économistes et rappeler le cadre statistiques de l'étude d'effets quantifiables !).

Référence à citer : https://clauswilke.com/dataviz/


Pour obtenir les données sur lesquels nous avons travaillé, nous avons utilisé plusieurs outils. 
-	Nous avons utilisé la librairie WorldFootballR disponible par un package qu’il suffit d’installer, pour ainsi appeler les fonctions dont on a besoin afin de collecter les données nécessaires. Cela reste très pratique car cette librairie nous permet de télécharger directement les résultats des matchs de la saison 2019 de Premier League par exemple, mais on peut le faire aussi pour beaucoup d’autres ligues et années. 

Nous avons eu à disposition 2 sites, Fbref et Transfermakt. 

-	FBref est une plateforme en ligne spécialisée dans les statistiques de football. Le site offre une gamme complète de données statistiques sur les joueurs, les équipes, les ligues et les compétitions de football du monde entier. Il propose des informations détaillées telles que les buts marqués, les passes décisives, les tirs au but, les interceptions et bien d'autres statistiques. 
-	Transfermarkt est une ressource en ligne majeure pour tout ce qui concerne les transferts de joueurs de football, les rumeurs de transferts, les valeurs marchandes des joueurs ainsi que les informations sur les contrats. Il offre une base de données exhaustive des joueurs, des clubs et des agents, ainsi que des détails sur les transferts passés et actuels.
Ce sont deux sites utiliser par différentes personnes comme les amateurs de football, les journalistes et les professionnels pour rester informés sur les évolutions au cours de la saison ou pendant les trêves/mercatos.

Concernant la fiabilité, ce sont des sites très utilisés et considérés comme fiable. Fbref est entretenu par l’entreprise Sport Reference qui gère également d'autres sites spécialisés dans les statistiques sportives, comme Baseball-Reference et Basketball Reference. Les données sur Fbref sont souvent vérifiées et mises à jour régulièrement, ce qui contribue à leur fiabilité. Pour Transfermakt, c’est aussi un site très utilisé pour les rumeurs de transferts et les transferts en général, il a une réputation de site fiable. Le site recueille des données sur les transferts, les valeurs marchandes des joueurs et d'autres détails liés aux contrats à partir de diverses sources, y compris les médias et les communiqués officiels des clubs. Cependant, c’est un site reliant des rumeurs de transferts, donc il peut y avoir des inexactitudes ou des spéculations qui ne se concrétisent pas toujours. Il est donc conseillé de vérifier les informations avec d'autres sources fiables, notamment lorsqu'il s'agit de transferts non confirmés.
