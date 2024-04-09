---
title: Head coach dismissal effect on football team performance
subject: Statistical analysis
short_title: Paper
banner: ./misc/banner.jpg
license: CC-BY-4.0
keywords: coach dismissal, team performance
date: 02/10/2024
downloads:
  - file: https://raw.githubusercontent.com/mathisdrn/head_coach_dismissal/master/exports/head_coach_dismissal.pdf
    title: Download PDF version
    filename: head_coach_dismissal.pdf
exports:
  # - format: typst
  #   template: lapreprint-typst
  #   output: ./exports/head_coach_dismissal.pdf
  #   articles:
  #       - file: Paper.md
  - format: pdf
    template: arxiv_two_column
    output: ./exports/head_coach_dismissal_arxiv.pdf
    articles:
        - file: Paper.md
  - format: pdf
    template: lapreprint
    output: ./exports/head_coach_dismissal_lapreprint.pdf
    articles:
        - file: Paper.md
  - format: pdf
    template: arxiv_nips
    output: ./exports/head_coach_dismissal_arxiv_nips.pdf
    articles:
        - file: Paper.md
---

+++ {"part": "abstract"}
This paper aims to explore the relationship between the team's performance and sports coach. To do that, we use traditional statistical methods applied to Men’s Football First Divisions of major leagues between 2017 and 2022. We investigate this relation on three different aspects: the effect of head coach tenure, the effect of regular renewal of sports coach by club, and the effect of changing clubs on the coach's performance. Our results show that there is a positive correlation between head coach tenure and team's performance, while the regular renewal of a sports coach by a club has a negative relation on the team's performance. We also find that head coach who regularly change club is negatively correlated with team's performance. These results suggest that stability and continuity are important factors for the success of a football team.
+++

## Introduction 

### Cadre de la problématique

% Écrire l'introduction

### Source des données

Les données utilisés au cours de cette analyse sont extraites de deux sites spécialisés dans les statistiques de football : [Fbref](https://fbref.com/) et [Transfermakt](https://www.transfermarkt.com/). 

- FBref offre une gamme complète de données statistiques sur les joueurs, les équipes, les ligues et les compétitions de football du monde entier. Il propose des informations détaillées telles que les buts marqués, les passes décisives, les tirs au but, les interceptions et bien d'autres statistiques.

- Transfermarkt est une ressource en ligne majeure pour tout ce qui concerne les transferts de joueurs de football, les rumeurs de transferts, les valeurs marchandes des joueurs ainsi que les informations sur les contrats. Il offre une base de données exhaustive des joueurs, des clubs et des agents, ainsi que des détails sur les transferts passés et actuels.

Ces sites sont utilisés par les amateurs de football, les journalistes et les professionnels pour rester informés sur les évolutions au cours de la saison ou pendant les trêves/mercatos.

### Fiabilité des données 

Ces sites sont très utilisés et considérés comme fiable. Fbref est entretenu par l’entreprise Sport Reference qui gère également d'autres sites spécialisés dans les statistiques sportives, comme Baseball-Reference et Basketball Reference. Les données sur Fbref sont souvent vérifiées et mises à jour régulièrement, ce qui contribue à leur fiabilité. Pour Transfermakt, c’est aussi un site très utilisé pour les rumeurs de transferts et les transferts en général, il a une réputation de site fiable. Le site recueille des données sur les transferts, les valeurs marchandes des joueurs et d'autres détails liés aux contrats à partir de diverses sources, y compris les médias et les communiqués officiels des clubs. Cependant, c’est un site reliant des rumeurs de transferts, donc il peut y avoir des inexactitudes ou des spéculations qui ne se concrétisent pas toujours. Il est donc conseillé de vérifier les informations avec d'autres sources fiables, notamment lorsqu'il s'agit de transferts non confirmés

### Références et outils utilisés

L'intégralité du travail de récupération, de pré-traitement, d'analyse et visualisation des données a été réalisé au sein de Notebook Jupyter. 

La récupération des données footballistique a été effectué à l'aide du package R [WorldFootBallR](https://github.com/JaseZiv/worldfootballR/). Ce package est régulièrement mis à jour et implémente des outils de web scraping afin d'extraire les données des principaux sites footballistiques.

Le pré-traitement, l'analyse et la visualisation des données a été effectué sous Python à l'aide de librairies standards : Pandas, Numpy, Matplotlib, Seaborn, Scipy, Statsmodels et Scikit-learn. 

La création d'un tableau de bord interactif a été réalisé à l'aide de la librairie ipywidgets.

L'écriture de ce papier a été réalisé dans un fichier Markdown.

[MyST](https://mystmd.org/) fait partie d'un écosystème d'outils qui chercher à améliorer le travail de communication scientifique en favorisant le développement d'une science reproducible et indexable. Cet outil a été utilisé pour permettre la diffusion de ce papier de recherche au format d'un [site statique](https://mathisdrn.github.io/head_coach_dismissal/) et d'un [PDF](https://raw.githubusercontent.com/mathisdrn/head_coach_dismissal/master/exports/head_coach_dismissal.pdf) répondant aux exigences de qualité scientifique.

MyST permet de réutiliser les entrées et les sorties des Notebooks Jupyter. Ainsi l'ensemble des figures, tableaux et une majorité des variables présentes dans ce papier sont directement issus des Notebooks Jupyter. À titre d'exemple, il est possible de renouveller l'intégralité de l'étude à d'autres ligues ou d'autres périodes en modifiant simplement les valeurs des variables utilisées dans les Notebooks Jupyter :

```{code} r
:filename: 00 Data extraction.ipynb
country <- c("ENG", "ESP", "ITA", "GER", "FRA")
year <- c(2018, 2019, 2020, 2021, 2022)
```

Enfin, la lecture de @DataViz a permis d'améliorer la qualité des graphiques et de la présentation des données en les rendants plus clairs et informatifs.

## Extraction des données

L'extraction se fait aisément à l'aide de [WorldFootballR](https://github.com/JaseZiv/worldfootballR/). 

Un premier jeu de données concernant les matchs est récupéré à partir de [Fbref](). Il contient des informations sur les matchs de football, notamment les équipes qui ont joués, le score final, le lieu du match et la date du match.
Un second jeu de données concernant les entraîneurs sportifs est récupéré à partir de [Transfermakt](). Il contient des informations sur les entraîneurs de football, notamment leur nom, leur date de naissance, leur nationalité, les dates de début et de fin de leur mandat, ainsi que des statistiques sur les matchs qu'ils ont dirigés.

## Pré-traitement des données

% Paragraphe introductif + préciser que les données seront présentés après le pré-traitement

:::{table} Extrait du jeu de donnée des résultats de matchs
:label: match-results1
![](#match_results)
:::

```{embed} #split_match_results
```

:::{table} Extrait du jeu de donnée sur les mandats des entraîneurs sportif
:label: head_coach1
![](#head_coach)
:::

On filtre dans un premier temps les entraîneurs qui n'ont pas été actif entre 2017 et 2022.

De plus, en vérifiant la qualité des données, nous avons remarqué qu'il existait parfois plus d'un coach pour une même période donnée :

```{embed} #overlapping_coach
```

:::{table} Example of inconsistency in the head coach data
:label: hc_inconsistency1
![](#hc_inconsistency)
:::

On exclu ces enregistrements du jeu de donnée.

```{embed} #join_head_coach_match
```

```{embed} #inconsistent_team_names
```

L'algorithme de la distance Levenshtein [@Levenshtein1965BinaryCC] a été utilisé pour faire correspondre les noms des équipes. Cet algorithme permet de calculer la distance entre deux chaînes de caractères en mesurant le nombre minimum d'opérations nécessaires pour transformer une chaîne en une autre.

```{code} python
:caption: Utilisation de l\'algorithme de la distance Levenshtein
:linenos:
from thefuzz import process

team_name_mapping = {}

for coach_team in coach_teams:
    matching_scores = process.extract(coach_team, match_teams, limit=1)
    
    if len(matching_scores) != 0 and matching_scores[0][1] >= 60:
        team_name_mapping[coach_team] = matching_scores[0][0]
    else:
        team_name_mapping[coach_team] = None
        print(f"No match found for {coach_team}")
```
:::{table} Exemple de correspondance des noms d'équipes
:label: team_match_table1
![](#team_match_table)
:::

L'ancienneté du coach sportif au sein de l'équipe lors du match est ajouté à chaque ligne des données de résultat de match. Le tableau suivant est ainsi obtenu :

:::{table} Extrait du jeu de donnée sur les matchs après pré-traitement
:label: final_match_results1
![](#final_match_results)
:::

## Présentation des données

```{embed} #match_data_summary
````

:::{table} Summary of the match data
:label: data_summary1
![](#data_summary)
:::

### L'avantage de jouer à domicile

:::{embed} #home_advantage_text
:::

:::{figure} #venue_effect
:name: venue_effect1
Venue effect on team's performance (2017 - 2022)
:::

### Les dynamiques temporelles

Les saisons de football sont divisées en deux périodes : la saison régulière et la saison hors-saison. La saison régulière est la période pendant laquelle les équipes jouent des matchs de championnat et de coupe, tandis que la saison hors-saison est la période pendant laquelle les équipes se préparent pour la saison suivante, notamment en recrutant de nouveaux joueurs et en changeant d'entraîneur.

:::{figure} #match_distribution
:name: match_distribution1
Monthly Distribution of Matches (2017 - 2022)
:::

% Ajouter describution figure


:::{figure} #hc_appointment 
:name: hc_appointment1
Monthly Distribution of Head Coaches Appointments
:::

:::{figure} #hc_dismissal 
:name: hc_dismissal1
Monthly Distribution of Head Coaches Dismissals
:::

Les licenciements d'entraîneurs sportif sont plus fréquents en fin de saison (voir [](#hc_appointment1)), tandis que les nominations d'entraîneurs sportif sont plus fréquentes en début de saison (voir [](#hc_dismissal1)). Cela peut s'expliquer par le fait que les clubs cherchent à renouveler leur effectif et à se donner les meilleures chances de succès pour la saison suivante.

## Analyse statistique

### Définitions

Le coefficient de corrélation de Pearson (valeur de r) est une mesure statistique qui évalue la force et la direction de la relation linéaire entre deux variables continues. Il est souvent utilisé pour quantifier la relation entre deux variables. 
- Lorsqu'il est de 1, il indique une corrélation linéaire parfaite positive.
- Lorsqu'il est de -1, il indique une corrélation linéaire parfaite négative.
- De plus, lorsqu'il est de 0, cela signifife qu'il n'y a aucune correlation linéaire entre les deux variables.

La p-value (valeur de p) est une mesure statistique utilisée pour déterminer la signification statistique d'un résultat. Dans le contexte de la corrélation de Pearson, la p-value est utilisée pour évaluer si la corrélation observée entre deux variables est statistiquement significative ou non. Si la p-value est inférieure à seuil, de 5% par exemple, on rejette l'hypothèse selon laquelle il n'y a pas de corrélation dans la population, et on conclut qu'il y a une corrélation significative entre les deux variables.

### L'effet du changement de club sur la performance du coach

% Paragraphe introductif

:::{figure} #club_per_hc
:name: club_per_hc1
Proportion of Head Coaches by Number of Club Appointments (2017 - 2022)
:::

Au cours de la période 2017 - 2022, plus de 55% des entraîneurs sportifs n'ont entrainé qu'un seul club. Environ 30% des entraîneurs ont entraîné 2 clubs et seulement 10% des entraîneurs ont entraîné plus de 3 clubs au cours de cette période (voir [](#club_per_hc1)).

:::{figure}
:name: hc_results_over_club_count
:align: center

(hc_win_vs_cc)=
![Win Ratio of Head Coaches versus Number of Clubs Appointments](#hc_win_ratio_over_club_count)

(hc_draw_vs_cc)=
![Draw Ratio of Head Coaches versus Number of Clubs Appointments](#hc_draw_ratio_over_club_count)

(hc_loss_vs_cc)=
![Loss Ratio of Head Coaches versus Number of Clubs Appointments](#hc_loss_ratio_over_club_count)

Performance of Head Coaches versus Number of Clubs Appointments
:::

La [](#hc_results_over_club_count) s'intéresse aux ratios de victoires, de matchs nuls et de défaites des entraîneurs en fonction du nombre de clubs pour lesquels ils ont travaillés durant la saison 2017 - 2022. Ces graphiques permettent de visualiser la relation entre la mobilité des entraîneurs et la performance de leurs équipes. Ainsi, nous observons :
- [({number})](#hc_win_vs_cc) une corrélation positive faible statistiquement significative (r = 0.19, p = 0.01), entre le nombre de clubs entraînés par le coach et son ratio de victoires.
- [({number})](#hc_draw_vs_cc) une corrélation négative faible non statistiquement significative (r = -0.09, p = 0.25), entre le nombre de clubs entraînés par le coach et son ratio de matchs nuls.
- [({number})](#hc_loss_vs_cc) une corrélation négative faible statistiquement significative (r = -0.18, p = 0.02), entre le nombre de clubs entraînés par le coach et son ratio de défaites.

Ces graphiques suggèrent que le nombre de clubs pour lesquels un entraîneur a travaillé a un impact positif sur la performance des équipes qu'il entraine. Cela pourrait s'expliquer par le fait que les entraîneurs qui ont travaillé pour plusieurs clubs ont une plus grande expérience et une meilleure connaissance du jeu, ce qui peut les aider à obtenir de meilleurs résultats. Il est aussi envisageable que les entraîneurs performant soit davantage reconnu et donc sollicité par d'autres clubs, favorisant ainsi leur mobilité entre les clubs.

Il reste néanmoins impossible d'établir une relation de causalité entre ces deux variables à l'aide de cette analyse. De nombreux autres facteurs peuvent influencer la performance des équipes, comme la qualité des joueurs, la stratégie de jeu, la gestion du club, etc.

### L'effet du renouvellement régulier du coach sur la performance de l'équipe

% Paragraphe introductif

:::{figure} #hc_per_club
:name: hc_per_club1
Proportion of Clubs by Number of Head Coaches Appointed (2017 - 2022)
:::

La [](#hc_per_club1) nous informe quand à la distribution du nombre d'entraîneurs employés par les clubs durant la période 2017 - 2022. On observe que plus de 85% des clubs ont employés au moins 3 entraîneurs différents suggérant qu'il y a un renouvellement régulier des entraîneurs dans les clubs de football.

:::{figure} #hc_per_club_per_league
:name: hc_per_club_per_league1
Average Number of Head Coaches Appointed per Club versus League (2017 - 2022)
:::

La [](#hc_per_club_per_league1) montre que les entraîneurs de la Premier League restent en poste plus longtemps que ceux des autres ligues. De plus, les équipes de la Premier League changent moins souvent d'entraîneur que celles des autres ligues. À l'inverse, la LaLiga renouvelle fréquemment ses entraîneur.

:::{figure} #club_win_ratio_over_coach_count
:name: club_win_ratio_over_coach_count1
Win Ratio of Clubs versus Number of Head Coaches Appointed by Club
:::

:::{figure} #club_draw_ratio_over_coach_count
:name: club_draw_ratio_over_coach_count1
Draw Ratio of Clubs versus Number of Head Coaches Appointed by Club
:::

:::{figure} #club_loss_ratio_over_coach_count
:name: club_loss_ratio_over_coach_count1
Loss Ratio of Clubs versus Number of Head Coaches Appointed by Club
:::

Les [](#club_win_ratio_over_coach_count1), [](#club_draw_ratio_over_coach_count1) et [](#club_loss_ratio_over_coach_count1) s'intéressent aux ratios de victoires, de matchs nuls et de défaites des clubs en fonction du nombre d'entraîneurs nommés à la tête de l'équipe durant la période 2017 - 2022. Ces relations pourraient montrer l'effet de la fréquence de remplacement d'un coach sur les performances de l'équipe. Ainsi, nous observons :
- Pour les victoires, une corrélation négative de faible à modérée (r = −0.27) statistiquement significative (p = 0.03).
- Pour les matchs nuls, une corrélation positive de faible à modérée (r=0.25) statistiquement significative (p = 0.04).
- Pour les défaites, une corrélation positive de faible à modérée (r=0.24) statistiquement significative (p = 0.05).

Ces résultats suggèrent que le renouvellement régulier des entraîneurs a un impact négatif sur les performances des équipes.
Cela pourrait s'expliquer par le fait que les entraîneurs ont besoin de temps pour s'adapter à leur nouvel environnement et pour mettre en place leur stratégie de jeu. De plus, les entraîneurs qui restent plus longtemps à la tête de l'équipe ont tendance à mieux connaître les joueurs et à mieux comprendre les forces et les faiblesses de l'équipe, ce qui peut contribuer à améliorer les performances de l'équipe.

### L'effet de l'ancienneté du coach sur la performance de l'équipe 

% paragraphe introductif

:::{figure} #hc_tenure 
:name: hc_tenure1
Empirical Cumulative Distribution Function of Head Coaches Tenure For Completed Appointments
:::

Plus de 50% des entraîneurs sportifs sont renouvelés après 1 an de mandat.
Ce pourcentage augmente à 80% après 2 ans de mandat et à 90% après 3 ans de mandat (voir [](#hc_tenure1))

:::{figure} #hc_tenure_per_league 
:name: hc_tenure_per_league1
Average Head Coach Tenure for Completed Appointments per League
:::

Les [](#hc_tenure_per_league1)  à l'ancienneté des entraîneurs sportif et au renouvellement des entraîneurs sportifs par rapport aux ligues d'interêt.

:::{figure} #hc_win_ratio_over_days
:name: hc_win_ratio_over_days1
Win Ratio of Head Coaches Appointments versus Head Coach Tenure
:::

:::{figure} #hc_draw_ratio_over_days
:name: hc_draw_ratio_over_days1
Draw Ratio of Head Coaches Appointments versus Head Coach Tenure
:::

:::{figure} #hc_loss_ratio_over_days
:name: hc_loss_ratio_over_days1
Loss Ratio of Head Coaches Appointments versus Head Coach Tenure
:::

Les [](#hc_win_ratio_over_days1) et [](#hc_draw_ratio_over_days1) et [](#hc_loss_ratio_over_days1) s'intéressent aux différents ratios de victoires, de matchs nuls et de défaites en fonction de la durée du coach au sein du club. Cette analyse permet de mettre en évidence le lien existant entre les résultats directs du coach et la durée de son mandat à la tête de l'équipe.
- Les valeurs des coefficients pour les victoires sont : r=0.36 et p=0.00. Cela indique une corrélation positive modérée et statistiquement significative (avec p<0.05) entre les deux variables étudiées.
- Pour les matchs nuls, r=−0.12 et p=0.05. Ainsi, il existe une corrélation linéaire faible et négative entre les deux variables, ce qui est statistiquement significatif selon le seuil de significativité choisi (ici, p=0.05).
- Quant aux défaites, r=−0.35 et p=0.00, cela indique une corrélation modérée négative et statistiquement significative entre les deux variables étudiées.

Il est à noter que les trois corrélations sont statistiquement significatives, étant donné que les valeurs de p sont inférieures (ou égales) à 0.05, qui est notre seuil d'acceptation. Ainsi, selon le coefficient de corrélation de Pearson 
r, nous observons que lorsque qu'un entraîneur gagne ses matchs, il augmente en même temps sa durée à la tête de l'équipe. En revanche, pour les défaites, plus il y en a, moins longtemps il reste coach de l'équipe. Les résultats neutres, représentés par les matchs nuls, ne jouent pas en faveur du coach, étant considérés comme un résultat moyen voire mauvais (r négatif). Par conséquent, plus il y aura de matchs nuls, plus la durée du coach en tant que leader de l'équipe diminuera.

#### Lien plus fin entre ancienneté du coach et performance de l'équipe

% Paragraphe introductif

:::{figure} #match_distribution_over_coach_tenure
:name: match_distribution_over_coach_tenure1
Distribution of Matches versus Head Coach Tenure on Match Day
:::

% Expliquer le graphique

:::{figure} #win_over_coach_tenure
:name: win_over_coach_tenure1
Match Win Outcome versus Head Coach Tenure on Match Day
:::

:::{figure} #draw_over_coach_tenure
:name: draw_over_coach_tenure1
Match Draw Outcome versus Head Coach Tenure on Match Day
:::

:::{figure} #loss_over_coach_tenure
:name: loss_over_coach_tenure1
Match Loss Outcome versus Head Coach Tenure on Match Day
:::

L'ancienneté, tout entraîneurs confondus a un effet positif sur la performance de l'équipe. Cela peut s'expliquer par le fait que les entraîneurs ont besoin de temps pour s'adapter à leur nouvel environnement et pour mettre en place leur stratégie de jeu. De plus, les entraîneurs qui restent plus longtemps à la tête de l'équipe ont tendance à mieux connaître les joueurs et à mieux comprendre les forces et les faiblesses de l'équipe, ce qui peut contribuer à améliorer les performances de l'équipe.
Néanmoins, il est aussi probable que les équipes qui ont de bons résultats ont tendance à garder leur entraîneurs plus longtemps, ce qui peut expliquer en partie la corrélation positive entre l'ancienneté du coach et la performance de l'équipe.

#### Une visualisation graphique de l'effet de l'ancienneté du coach sur la performance de l'équipe

:::{figure} #match_outcome_over_coach_tenure
:name: match_outcome_over_coach_tenure1
Weighted Rolling Average of Match Outcome versus Head Coach Tenure on Match Day
:::

Le [graphique](#match_outcome_over_coach_tenure1) illustre la proportion des résultats des matchs en fonction de l'ancienneté de l'entraîneur principal lors du match. Cette proportion est calculé à l'aide d'une moyenne pondérée sur une période de 100 jours. La zone verte représente les victoires, la zone grise représente les matchs nuls et la zone rouge représente les défaites. On peut observer que les victoires tendent à augmenter avec l'ancienneté de l'entraîneur, tandis que les défaites ont tendance à diminuer.

:::{code} python
:caption: Calcul des moyennes mobiles pondérées
:linenos:
import numpy as np

def weighted_rolling_mean(data, weights, window_size=30):
    def weighted_mean(x):
        return np.average(data.loc[x.index], weights=weights.loc[x.index])

    return data.rolling(window_size, min_periods=1).apply(weighted_mean, raw=False)
:::

## Conclusion

L'analyse des données a permis de mettre en évidence l'effet du licenciement d'un coach sur la performance de l'équipe. Les résultats montrent que l'ancienneté du coach au sein de l'équipe est corrélée positivement avec la performance de l'équipe. En d'autres termes, plus un coach reste longtemps à la tête de l'équipe, meilleures sont les performances de l'équipe. De plus, le renouvellement régulier d'un coach sportif est corrélé négativement avec la performance de l'équipe. Ces résultats suggèrent que la stabilité et la continuité sont des facteurs importants pour la réussite d'une équipe de football.
Dans la seconde séries de graphiques nous avons montrée que les clubs qui renouvelle régulièrement leur coach ont tendance à voir une dégradation de leurs performances. 
Dans la troisième série de graphiques nous montrons que les entraîneurs qui changent régulièrement de club ont tendance à voir une amélioration de la performance de l'équipe.
Cela semble indiquer qu'un renouvellement régulier des entraîneurs peut être bénéfique pour l'équipe, mais que la stabilité et la continuité d'un coach peuvent également avoir un impact significatif sur les performances de l'équipe, en particulier à court terme.

Cependant, il est difficile de tirer des conclusions définitives sur la causalité de ces relations, car il existe de nombreux autres facteurs qui peuvent influencer la performance d'une équipe de football. Par exemple, la qualité des joueurs, la stratégie de jeu, la gestion du club et d'autres facteurs peuvent également jouer un rôle important dans la performance de l'équipe. Il est donc important de prendre en compte ces facteurs lors de l'analyse des données et de ne pas tirer de conclusions hâtives sur la relation entre le licenciement d'un coach et la performance de l'équipe.

+++ {"part": "data_availability"}
L'ensemble des fichiers et données relatif à ce travail sont disponible en accès libre sur le [dépot GitHub](https://github.com/mathisdrn/head_coach_dismissal) sous licence MIT.
+++