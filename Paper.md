---
title: Head coach dismissal effect on football team performance
subject: Statistical analysis
short_title: Paper
banner: ./misc/banner.jpg
license: CC-BY-4.0
keywords: 
    - coach dismissal
    - team performance
date: 2024-04-14
---

+++ {"part": "abstract"}
This paper aims to explore the relationship between the team's performance and sports coach. To do that, we use traditional statistical methods applied to Men’s Football First Divisions of major leagues between 2015 and 2023. We investigate this relation on three different aspects: the effect of head coach tenure, the effect of regular renewal of sports coach by club, and the effect of changing clubs on the coach's performance. Our results show that there is a positive correlation between head coach tenure and team's performance, while the regular renewal of a sports coach by a club has a negative relation on the team's performance. We also find that head coach who regularly change club is negatively correlated with team's performance. These results suggest that stability and continuity are important factors for the success of a football team.
+++

## Introduction 

Le football est un sport populaire qui attire des millions de fans à travers le monde. Les équipes de football sont composées de joueurs talentueux, mais elles sont également dirigées par des entraîneurs sportifs qui jouent un rôle crucial dans le succès de l'équipe. Les entraîneurs sportifs sont responsables de la stratégie de jeu, de la tactique, de la motivation des joueurs et de la gestion de l'équipe. Ils sont souvent considérés comme les architectes du succès d'une équipe.

Au cours des dernières années, de nombreuses équipes de football ont connu des changements fréquents d'entraîneurs sportifs. Ces changements peuvent être dus à divers facteurs, tels que les mauvais résultats de l'équipe, les conflits internes, les différends avec les joueurs ou la direction du club, ou simplement le désir de renouveler l'équipe. Cependant, il est important de comprendre l'impact de ces changements d'entraîneurs sur la performance de l'équipe.

Dans cette étude, nous allons analyser les données des ligues de football masculin de première division de cinq pays européens (Angleterre, Espagne, Italie, Allemagne et France) sur la période 2015 - 2023. 

Cette analyse vise à mieux comprendre la relation entre la performance d'une équipe de football et l'entraîneur sportif. Nous allons nous intéresser à trois aspects différents de cette relation : l'effet de l'ancienneté de l'entraîneur sur la performance de l'équipe, l'effet du renouvellement régulier de l'entraîneur par le club sur la performance de l'équipe, et l'effet du changement de clubs sur la performance de l'entraîneur.

### Source des données

Les données utilisées au cours de cette analyse sont extraites de deux sites spécialisés dans les statistiques de football : [Fbref](https://fbref.com/) et [Transfermakt](https://www.transfermarkt.com/). 

FBref met à disposition une grande quantité de données sur les les matchs, les joueurs, les équipes et les compétitions de football. Il fournit des informations détaillées sur les performances des joueurs, les statistiques de match, les classements des équipes, les résultats des matchs et d'autres données liés au football.

Fbref est détenu par l’entreprise Sport Reference qui gère également d'autres sites spécialisés dans les statistiques sportives, comme Baseball-Reference et Basketball Reference.

Transfermarkt est un site spécialisé dans les transferts de joueurs de football. Il fournit des informations sur les transferts de joueurs, les valeurs marchandes des joueurs, les contrats des joueurs, les rumeurs de transferts et d'autres détails liés aux transferts de joueurs.

Ces sites sont utilisés par les fans de football, les médias, les clubs de football et les professionnels du football pour obtenir des informations footballistique.

### Fiabilité des données 

Ces sites sont considérés comme fiable. Ils sont régulièrement mis à jour et vérifiés pour assurer la qualité et la précision des données. Les données sont collectées à partir de sources officielles, comme les ligues de football, les clubs de football, les fédérations de football et d'autres sources fiables. Les données sont ensuite vérifiées et validées par des experts en statistiques sportives avant d'être publiées sur les sites.

### Références et outils utilisés

L'intégralité du travail de récupération, de pré-traitement, d'analyse et visualisation des données a été réalisé au sein de Notebook Jupyter. 

La récupération des données footballistique a été effectuée à l'aide du package R [WorldFootBallR](https://github.com/JaseZiv/worldfootballR/). Ce package est régulièrement mis à jour et implémente des outils de web scraping afin d'extraire les données des principaux sites footballistiques.

Le pré-traitement, l'analyse et la visualisation des données a été effectué sous Python à l'aide de librairies standards : Pandas, Numpy, Matplotlib, Seaborn, Scipy.

L'écriture de ce papier a été réalisé dans un fichier au format Markdown.

[MyST](https://mystmd.org/) fait partie d'un écosystème d'outils qui chercher à améliorer le travail de communication scientifique en favorisant le développement d'une science reproducible et indexable. Cet outil a été utilisé pour permettre la diffusion de ce papier de recherche au format d'un [site statique](https://mathisdrn.github.io/head_coach_dismissal/) et d'un [PDF](https://raw.githubusercontent.com/mathisdrn/head_coach_dismissal/master/exports/head_coach_dismissal.pdf) répondant aux exigences de qualité scientifique.

MyST permet de réutiliser les entrées et les sorties des Notebooks Jupyter. Ainsi l'ensemble des figures, tableaux et une partie des variables présentes dans ce papier sont directement issus des Notebooks Jupyter. À titre d'exemple, il est possible de renouveller l'intégralité de l'étude à d'autres ligues ou d'autres périodes en modifiant simplement les valeurs des variables utilisées dans les Notebooks Jupyter :

:::{code} r
:filename: 00 Data extraction.ipynb
country <- c("ENG", "ESP", "ITA", "GER", "FRA")
year <- c(2015:2022)
:::

Enfin, la lecture de Fundamentals of Data Visualization [@DataViz] a permis d'améliorer la qualité des graphiques et de la présentation des données en les rendants plus clairs et informatifs.

## Préparation des données

Il est essentiel de préparer les données avant de les analyser. Cette étape consiste à nettoyer les données, à les transformer et à les organiser de manière à ce qu'elles soient exploitables pour l'analyse statistique. De plus, il est important de vérifier l'intégrité et la complétude des données afin de s'assurer de leur cohérence et de leur fiabilité dans le cadre de l'analyse statistique.

Ces différentes étapes de préparation des données sont réalisées de manière itérative et suivent rarement un chemin linéaire. L'évolution des besoins de l'étude, les contraintes imposées par les données disponibles et les données d'intérêts et la détection d'incohérences dans les données sont autant de facteurs qui amènent à faire évoluer la pipeline de préparation des données. Davantage de détails sur le traitement des données sont disponibles dans les Notebooks Jupyter associés à ce papier.

### Données extraites 

Un premier jeu de donnée concernant les matchs est récupéré à partir de [Fbref](). Il contient des informations sur les matchs de football, notamment les équipes qui ont joué, le score final, le lieu du match et la date du match.

:::{table} Extrait du jeu de donnée sur les matchs
:label: match_results1
:align: center
![](#match_results)
:::

Un second jeu de donnée concernant les mandats des entraîneurs chef est récupéré à partir de [Transfermakt](). Il contient la date de début et de fin du mandat d'un entraîneur sportif, le club concerné, ainsi que nom et la performance agrégé de l'entraîneur lors de ce mandat.

:::{table} Extrait du jeu de donnée sur les mandats des entraîneurs sportif
:label: head_coach1
:align: center
![](#head_coach)
:::

### Données d'intérêt

On exclut des données de résultat de matchs, les matchs ne concernant pas les équipes de première division.

On exclut des mandats des entraîneurs, les entraîneurs sportifs n'ayant pas été actifs entre le début de la saison 2015 et la fin de la saison 2023.

On exclut des mandats des entraîneurs, les entraîneurs sportifs ayant eu moins de 5 matchs à la tête d'une équipe. En effet, ces entraîneurs sont soit des entraîneurs de substitution, qui sont intervenus pour une courte période avant d'être remplacé par un entraîneur permanent, soit des entraîneurs qui ont été licenciés rapidement en raison d'une faute professionnelle ou d'une incompatibilité entre l'équipe et l'entraîneur sportif.

### Données manquantes ou incohérentes

Certains matchs ne possèdent pas d'informations sur le résultat final. Ces matchs correspondent en réalité à des matchs qui ont été annulés ou reportés notamment en lien avec le COVID-19. Ces matchs sont exclus de l'analyse.

Certains enregistrements de mandats d'entraîneurs ne possèdent pas d'information sur le pays et la ligue du club concerné. Ces informations ont été ajoutées manuellement en se basant sur le nom du club avant le filtrage sur les données d'intérêts.

Un nombre important d'équipe a des informations incomplètes sur les mandats des entraîneurs sportifs. Certaines de ces données manquantes correspondent à des périodes de changement d'entraîneurs, durant laquelle le club n'a plus d'entraîneur sportif en poste.
Toutefois, un nombre significatif d'équipes ne possèdent aucune information sur l'entraîneur sportif à la tête du club entre 2015 et 2023. L'absence de mandat entre 2015 et 2023 concerne 95 équipes sur les 161 équipes d'intérêts. Le problème provient de la liste de liens TransferMarkt retournée par la fonction `tm_league_team_urls(country_name, start_year)` de worldfootballR qui ne contient pas l'ensemble des équipes des pays d'intérêts.

Ce problème a été détecté à la fin de l'analyse et n'a pas pu être corrigé. Une des solutions consisterait à ajouter manuellement les liens TransferMarkt des 95 équipes pour lesquelles il n'y a aucun enregistrement d'entraîneurs sportifs.

![](#overlapping_coach)

:::{table} Exemple d'inconsistences dans les données des entraîneurs sportifs
:label: hc_inconsistency1
:align: center
![](#hc_inconsistency)
:::

![](#inconsistent_team_names)

:::{table} Exemple de correspondance des noms d'équipes
:label: team_match_table1
:align: center
![](#team_match_table)
:::

Nous avons utilisé l'algorithme de la distance Levenshtein [@Levenshtein1965BinaryCC] afin de faire correspondre les équipes des mandats d'entraîneurs aux équipes des résultats de matchs. Nous restreignons par ailleurs la recherche d'une équipe correspondante à la liste des équipes du pays correspondant afin de limiter le nombre de correspondances possibles.
L'ajustement du score de Levenshtein a permis de rapidement vérifier la validité des correspondances de plus faible certitude.

:::{code} python
:caption: Utilisation de l\'algorithme de la distance Levenshtein
:linenos:
from thefuzz import process

team_name_mapping = {}

# For each country
for country in coach_teams_by_country.index:
    # Get teams for this country
    coach_teams = coach_teams_by_country[country]
    match_teams = match_teams_by_country.get(country, [])

    # For each team in coach_teams
    for coach_team in coach_teams:
        # Find the best match in match_teams
        matching_scores = process.extract(coach_team, match_teams, limit=1)

        if len(matching_scores) != 0 and matching_scores[0][1] >= 60:
            team_name_mapping[coach_team] = matching_scores[0][0]
        else:
            team_name_mapping[coach_team] = None
            print(f"No match found for {coach_team} among {match_teams} in {country}")
:::


### Transformation des données

Les [données sur les résultats des matchs](#match_results1) sont modifiés de manière à ce que chaque match soit divisé en deux lignes : une pour chaque équipe. Ainsi, chaque ligne représente le résultat d'une équipe lors d'un match : la date du match, le résultat final, la présence ou non de l'équipe à domicile, le score final de l'équipe ainsi que le nom de l'équipe.

De plus, nous ajoutons aux données de match l'ancienneté de l'entraîneur au sein de l'équipe lorsque ce match a été joué.

:::{table} Extrait du jeu de donnée sur les matchs après pré-traitement
:label: final_match_results1
:align: center
![](#final_match_results)
:::

Nous ajoutons également aux [données des mandats des entraîneurs sportifs](#head_coach1) le nombre de clubs pour lequel l'entraîneur a travaillé parmi les clubs des ligues et divisions d'intérêts.

## Présentation des données

![](#match_data_summary)

:::{table} Summary of the match data
:label: data_summary1
:align: center
![](#data_summary)
:::

### L'avantage de jouer à domicile

![](#home_advantage_text)

:::{figure} #venue_effect
:name: venue_effect1
:align: center
:height: 2em
:width: 2em
Venue effect on team's performance (2015 - 2023)
:::

### Les dynamiques temporelles

Les saisons de football sont divisées en deux périodes : la saison régulière et la saison hors-saison. La saison régulière est la période pendant laquelle les équipes jouent des matchs de championnat et de coupe, tandis que la saison hors-saison marque une période de pause permettant à l'équipe de s'entraîner et de se préparer pour la saison suivante.

:::{figure} #match_distribution
:name: match_distribution1
:align: center
Monthly Distribution of Matches (2015 - 2023)
:::

Une proportion importante des nominations et licenciement des entraîneurs sportifs a lieu en période de hors-saison (([](#hc_appointment1)) et [](#hc_dismissal1)). 
En effet, les clubs profitent de cette période pour revoir leur stratégie et renouveler certains membres de l'équipe. Le changement d'entraîneur au cours de la saison régulière est plus rare et risqué, car l'équipe est déjà engagée dans des compétitions et le changement d'entraîneur peut perturber la dynamique de l'équipe. Le licenciement d'un entraîneur en cours de saison pourrait indiquer une situation critique pour le club, comme une série de mauvais résultats ou des conflits internes.

:::{figure} #hc_appointment 
:name: hc_appointment1
:align: center
Monthly Distribution of Head Coaches Appointments
:::

:::{figure} #hc_dismissal 
:name: hc_dismissal1
:align: center
Monthly Distribution of Head Coaches Dismissals
:::

Les périodes de nominations et de licenciement des entraîneurs sportifs sont relativement stables au cours des saisons, mais aussi entre les ligues ([](#hc_season_break1)).

:::{figure} #hc_season_break
:name: hc_season_break1
:align: center
Proportion of in-season vs off-season head coach dismissal per league
:::

## Analyse statistique

### Définitions

Le coefficient de corrélation de Pearson (valeur de $r$) est une mesure statistique qui évalue la force et la direction de la relation linéaire entre deux variables continues. Il est souvent utilisé pour quantifier la relation entre deux variables. 
- Lorsque $r = 1$, cela indique une corrélation linéaire parfaite positive.
- Lorsque $r = -1$, cela indique une corrélation linéaire parfaite négative.
- De plus, lorsque $r = 0$, cela signifie qu'il n'y a aucune corrélation linéaire entre les deux variables.

La p-value (valeur de $p$) est une mesure statistique utilisée pour déterminer la signification statistique d'un résultat. Dans le contexte de la corrélation de Pearson, la p-value est utilisée pour évaluer si la corrélation observée entre deux variables est statistiquement significative ou non. Si la p-value est inférieure à un seuil (ici $p < 0.05$), on rejette l'hypothèse selon laquelle il n'y a pas de corrélation dans la population, et on conclut qu'il y a une corrélation significative entre les deux variables.

:::{caution}
Une p-valeur faible dans le cadre de la corrélation de Pearson ne signifie pas nécessairement qu'il existe une relation de cause à effet entre les deux variables observées. Elle indique simplement que la corrélation observée est statistiquement significative. Ainsi, les hypothèses explicatives fournies sont simplement des hypothèses plausibles et non des conclusions définitives.
:::

### Renouvellement de l'entraîneur et performance du club

Dans cette partie, nous allons étudier les effets de la fréquence de renouvellement des coachs sur la performance d'une équipe. L'objectif est de voir les effets sur les résultats obtenus lorsque qu'une équipe change régulièrement d'entraîneur.

La [](#hc_per_club1) nous informe quant à la distribution du nombre d'entraîneurs employés par les clubs durant la période 2015 - 2023. On observe que plus de 85 % des clubs ont employés au moins 3 entraîneurs différents suggérant qu'il y a un renouvellement régulier des entraîneurs dans les clubs de football.

:::{figure} #hc_per_club
:name: hc_per_club1
:align: center
Proportion of Clubs by Number of Head Coaches Appointed (2015 - 2023)
:::

La [](#hc_per_club_per_league1) montre que les entraîneurs de la Premier League restent en poste plus longtemps que ceux des autres ligues. De plus, les équipes de la Premier League changent moins souvent d'entraîneur que celles des autres ligues. À l'inverse, la LaLiga renouvelle fréquemment ses entraîneurs.

:::{figure} #hc_per_club_per_league
:name: hc_per_club_per_league1
:align: center
Average Number of Head Coaches Appointed per Club versus League (2015 - 2023)
:::

La [](#club_results_over_coach_count) s'intéresse aux ratios de victoires, de matchs nuls et de défaites des clubs en fonction du nombre d'entraîneurs nommés à la tête de l'équipe au cours de la période 2015 - 2023. Ces graphiques permettent de visualiser la relation entre la fréquence de renouvellement des entraîneurs et la performance des équipes.

:::{figure}
:name: club_results_over_coach_count
:align: center

(club_win_vs_cc)=
![Club Win Ratio versus Number of Head Coaches Appointed by Club](#club_win_ratio_over_coach_count)

(club_draw_vs_cc)=
![Club Draw Ratio versus Number of Head Coaches Appointed by Club](#club_draw_ratio_over_coach_count)

(club_loss_vs_cc)=
![Club Loss Ratio versus Number of Head Coaches Appointed by Club](#club_loss_ratio_over_coach_count)

Clubs Results versus Number of Head Coaches Appointed by Club
:::

Ainsi, nous observons :
- [({number})](#club_win_vs_cc) une corrélation négative modérée ($r = −0.36$) statistiquement significative ($p = 0.00$) entre le nombre d'entraîneurs nommés par le club et son ratio de victoires.
- [({number})](#club_draw_vs_cc) une corrélation positive modérée ($r = 0.36$) statistiquement significative ($p = 0.00$) entre le nombre d'entraîneurs nommés par le club et son ratio de matchs nuls.
- [({number})](#club_loss_vs_cc) une corrélation positive faible ($r = 0.32$) statistiquement significative ($p = 0.01$) entre le nombre d'entraîneurs nommés par le club et son ratio de défaites.

Plusieurs hypothèses peuvent être émises pour expliquer ces résultats :
1. La performance de l'équipe comme facteur explicatif de la fréquence de renouvellement du coach :
    - Une équipe qui affiche de bons résultats a tendance à garder son entraîneur plus longtemps car il est une partie intégrante de la stabilité et de la performance actuelle de l'équipe. Aussi les entraîneurs choisissent de rester plus longtemps au sein d'un club qui affiche de bons résultats (avantages financiers, reconnaissance, satisfaction personnelle).
    - Une équipe qui affiche de mauvais résultats a tendance à renouveler ses entraîneurs plus fréquemment pour tenter d'améliorer ses performances. Aussi, les entraîneurs qui ne parviennent pas à obtenir de bons résultats sont plus susceptibles de quitter le club ou d'être licenciés.
2. La fréquence de renouvellement du coach comme facteur explicatif de la performance de l'équipe :
    - Les clubs qui gardent le même entraîneur pendant une longue période bénéficient de la stabilité et de la continuité dans la stratégie de jeu et la gestion de l'équipe, ce qui peut contribuer à améliorer les performances de l'équipe.
    - Les clubs qui choisissent de renouveler fréquemment leurs entraîneurs peuvent souffrir d'un manque de continuité et de stabilité dans la stratégie de jeu et la gestion de l'équipe, ce qui peut affecter négativement les performances de l'équipe. 
3. Existence de facteurs tiers qui affecte à la fois le renouvellement du coach et la performance de l'équipe 
    - Les clubs renouvellent fréquemment leurs entraîneurs en raison de problèmes internes ou de conflits avec les joueurs ou la direction du club, ce qui peut affecter négativement les performances de l'équipe.
    - Les clubs qui affichent de moins bon résultats sont moins attractifs pour les entraîneurs et les joueurs

### Mobilité des entraîneurs et performance des équipes

Ici, nous allons observer la relation entre les performances des entraîneurs et le nombre de clubs par lesquels ils sont passés. Cette relation nous permettra de voir si le nombre de clubs qu'un entraîneur a faits a un impact sur les résultats de l'équipe.

Au cours de la période 2017 - 2022, plus de 60 % des entraîneurs sportifs n'ont entraîné qu'un seul club. Environ 20 % des entraîneurs ont entraîné 2 clubs et seulement 10 % des entraîneurs ont entraîné plus de 3 clubs au cours de cette période (voir [](#club_per_hc1)).

:::{figure} #club_per_hc
:name: club_per_hc1
:align: center
Proportion of Head Coaches by Number of Club Appointments (2015 - 2023)
:::

La [](#hc_results_over_appointment_count) s'intéresse aux pourcentages de victoires, de matchs nuls et de défaites de chaque mandat des entraîneurs par rapport au nombre d'équipe qu'ils ont entraîné jusqu'à présent au sein des équipes d'intérêts pour la saison 2015 - 2023. Ces graphiques permettent de visualiser la relation entre l'expérience acquise par l'entraîneur au cours de son passage successif au sein de plusieurs clubs et l'impact sur la performance de leurs équipes.

:::{figure}
:name: hc_results_over_appointment_count
:align: center

(hc_win_vs_appointment_count1)= 
![Head Coach Appointment Win Ratio versus Appointment Count](#hc_win_vs_appointment_count)

(hc_draw_vs_appointment_count1)=
![Head Coach Appointment Draw Ratio versus Appointment Count](#hc_draw_vs_appointment_count)

(hc_loss_vs_appointment_count1)=
![Head Coach Appointment Loss Ratio versus Appointment Count](#hc_loss_vs_appointment_count)

Head Coach Appointment Performance versus Appointment Count
:::

Il n'existe pas de corrélation statistiques significative entre le nombre de clubs pour lesquels un entraîneur a travaillé et son pourcentage de victoires ($p = 0.95$), de matchs nuls ($p = 0.05$) ou de défaites ($p = 0.24$).

Il est possible que l'absence de corrélation stastiquement significative soit dû à l'absence d'une information complète sur l'expérience passés des entraîneurs.

La [](#hc_results_over_club_count) suivante diffère quant à elle car elle s'intéresse à la performance agrégée des entraîneurs au cours de leurs carrières au sein des équipes et saisons d'intérêt par rapport au nombre total de club pour lesquels ils ont travaillés durant la saison 2015 - 2023. Ces graphiques permettent de visualiser la relation entre la mobilité des entraîneurs et la performance de leurs équipes.

:::{figure}
:name: hc_results_over_club_count
:align: center

(hc_win_vs_cc)=
![Head Coach Aggregated Win Ratio versus Total Number of Appointments](#hc_win_ratio_over_club_count)

(hc_draw_vs_cc)=
![Head Coach Aggregated Draw Ratio versus Total Number of Appointments](#hc_draw_ratio_over_club_count)

(hc_loss_vs_cc)=
![Head Coach Aggregated Loss Ratio versus Total Number of Appointments](#hc_loss_ratio_over_club_count)

Performance of Head Coaches versus Number of Clubs Appointments
:::

Ainsi, nous observons :
- [({number})](#hc_win_vs_cc) une corrélation positive faible ($r = 0.18$) statistiquement significative ($p = 0.00$) entre le nombre de clubs entraînés par le coach et son ratio de victoires.
- [({number})](#hc_draw_vs_cc) une corrélation positive très faible ($r = 0.03$) mais statistiquement non significative ($p = 0.67$) entre le nombre de clubs entraînés par le coach et son ratio de matchs nuls.
- [({number})](#hc_loss_vs_cc) une corrélation négative faible ($r = -0.21$) statistiquement significative ($p = 0.00$) entre le nombre de clubs entraînés par le coach et son ratio de défaites.

Plusieurs hypothèses peuvent être émises pour expliquer ces résultats :
1. La performance de l'équipe comme facteur explicatif de la mobilité du coach :
    - Les entraîneurs qui obtiennent de bons résultats sont plus susceptibles d'être sollicités par d'autres clubs, ce qui peut expliquer pourquoi ils ont travaillé pour un plus grand nombre de clubs.
    - Les entraîneurs qui obtiennent de mauvais résultats sont potentiellement relégué à des ligues de division 2 ne faisant pas parti de nos ligues d'intérêts.
2. La mobilité du coach comme facteur explicatif de la performance de l'équipe :
    - Les entraîneurs qui ont travaillé pour un plus grand nombre de clubs ont acquis une expérience plus diversifiée et ont pu développer des compétences et des connaissances qui leur permettent d'obtenir de meilleurs résultats.
    - Les entraîneurs qui ont travaillé pour un plus petit nombre de club n'ont pas eu l'opportunité de développer des compétences et des connaissances aussi diversifiées, ce qui peut affecter négativement leurs performances et donc la performance de l'équipe.
3. Le biais des données : en effet, nous n'avons collecté que les données des entraîneurs qui ont été actifs entre 2015 et 2023 et pour les ligues d'interêts. Il est possible que les entraîneurs qui ont réussi leurs mandats soient plus susceptibles d'être sollicités par d'autres clubs faisant partie des ligues d'intérêts.

### Ancienneté de l'entraîneur et performance de l'équipe 

Dans cette partie, nous cherchons une éventuelle relation entre l'expérience qu'un entraîneur a pu accumuler avec son ancienneté et les performances de l'équipe lorsqu'il est à sa tête. L'ancienneté pourrait bien être un facteur important au sein d'une équipe, car l'entraîneur gagne en expérience au fil des clubs par lesquels il est passé. Mais cette expérience a-t-elle une réelle incidence sur les résultats obtenus ?

La [](#hc_tenure1) montre la distribution de l'ancienneté des entraîneurs sportifs au sein de leur club. On observe que plus de 50 % des entraîneurs sportifs sont renouvelés après 1 an de mandat. Ce pourcentage augmente à 80 % après 2 ans de mandat et à 90 % après 3 ans de mandat.

:::{figure} #hc_tenure 
:name: hc_tenure1
:align: center
Empirical Cumulative Distribution Function of Head Coaches Tenure For Completed Appointments
:::

La [](#hc_tenure_per_league1) montre que les entraîneurs de la Premier League restent en poste plus longtemps que ceux des autres ligues. De plus, les équipes de la Premier League changent moins souvent d'entraîneur que celles des autres ligues. À l'inverse, la LaLiga renouvelle fréquemment ses entraîneurs.

:::{figure} #hc_tenure_per_league 
:name: hc_tenure_per_league1
:align: center
Average Head Coach Tenure for Completed Appointments per League
:::

La [](#hc_results_over_tenure3) s'intéresse aux résultats des équipes durant le mandat d'un entraîneur en fonction de la durée du mandat de l'entraîneur. Cette analyse permet de mettre en évidence la relation entre l'ancienneté de l'entraîneur et la performance de l'équipe.

:::{figure}
:name: hc_results_over_tenure3
:align: center

(hc_win_vs_tenure)=
![Win Ratio of Head Coach Appointment versus Appointment Tenure](#hc_win_ratio_over_days)

(hc_draw_vs_tenure)=
![Draw Ratio of Head Coach Appointment versus Appointment Tenure](#hc_draw_ratio_over_days)

(hc_loss_vs_tenure)=
![Loss Ratio of Head Coach Appointment versus Appointment Tenure](#hc_loss_ratio_over_days)

Team Results of Head Coach Appointment versus Appointment Tenure
:::

Nous observons : 
- [({number})](#hc_win_vs_tenure) une corrélation positive modérée ($r = 0.38$) statistiquement significative ($p = 0.00$) entre la durée du mandat de l'entraîneur et le pourcentage de victoires.
- [({number})](#hc_draw_vs_tenure) une corrélation négative faible ($r = −0.05$) mais statistiquement-non significative ($p = 0.32$) entre la durée du mandat de l'entraîneur et le pourcentage de matchs nuls.
- [({number})](#hc_loss_vs_tenure) une corrélation négative modérée ($r = −0.38$) statistiquement significative ($p = 0.00$) entre la durée du mandat de l'entraîneur et le pourcentage de défaites.

Les hypothèses explicatives du lien entre la durée du mandat de l'entraîneur et la performance de l'équipe sont similaires aux hypothèses fournies pour expliquer le lien entre la fréquence du renouvellement des entraîneurs par les clubs et la performance du club :

1. La durée du mandat comme facteur explicatif de la performance de l'équipe :
    - Les entraîneurs qui restent plus longtemps à la tête de l'équipe ont tendance à mieux connaître les joueurs et à mieux comprendre les forces et les faiblesses de l'équipe, ce qui peut contribuer à améliorer les performances de l'équipe.
    - Les entraîneurs qui restent moins longtemps à la tête de l'équipe n'ont pas eu le temps de mettre en place leur stratégie de jeu et de s'adapter à leur nouvel environnement, ce qui peut affecter négativement les performances de l'équipe.
2. La performance de l'équipe comme facteur explicatif de la durée du mandat de l'entraîneur :
    - Les équipes qui obtiennent de bons résultats ont tendance à garder leur entraîneur plus longtemps, car il est une partie intégrante de la stabilité et de la performance actuelle de l'équipe.
    - Les équipe qui obtiennent de mauvais résultats ont tendance à renouveler leurs entraîneurs plus fréquemment pour tenter d'améliorer leurs performances.
3. Existence de facteurs tiers qui affecte à la fois la durée du mandat de l'entraîneur et la performance de l'équipe.

### Ancienneté de l'entraîneur lors du match

La [](#match_distribution1) montre la distribution des matchs en fonction de l'ancienneté de l'entraîneur lors du match. On observe qu'environ 63 % des matchs sont supervisé par un entraîneur ayant moins de 500 jours d'ancienneté au sein du club. 

:::{figure} #match_distribution_over_coach_tenure
:name: match_distribution_over_coach_tenure1
:align: center
Distribution of Matches versus Head Coach Tenure on Match Day
:::

La [](#match_result_over_coach_tenure) montre le résultat individuel des matchs en fonction de l'ancienneté du coach lors du match. Ce graphique permet de visualiser la relation entre l'ancienneté du coach lors du match et la performance de l'équipe lors de ce match. Néanmoins, aucune des corrélations observées n'est statistiquement significative.

:::{figure}
:name: match_result_over_coach_tenure
:align: center

(match_win_vs_days)=
![Match Win Outcome versus Head Coach Tenure on Match Day](#win_over_coach_tenure)

(match_draw_vs_days)=
![Match Draw Outcome versus Head Coach Tenure on Match Day](#draw_over_coach_tenure)

(match_loss_vs_days)=
![Match Loss Outcome versus Head Coach Tenure on Match Day](#loss_over_coach_tenure)


Match Outcome versus Head Coach Tenure on Match Day
:::

![](#match_stats)

La [](#match_outcome_vs_days) illustre la proportion des résultats des matchs en fonction de l'ancienneté de l'entraîneur principal lors du match. Cette proportion est calculée à l'aide d'une moyenne pondérée sur une période de 100 jours. La zone verte représente les victoires, la zone grise les matchs nuls et la zone rouge les défaites. On n'observe pas de tendance claire dans les résultats des matchs en fonction de l'ancienneté de l'entraîneur lors du match.

:::{figure} #match_outcome_over_coach_tenure
:name: match_outcome_vs_days
:align: center
Weighted Rolling Average of Match Outcome versus Head Coach Tenure on Match Day
:::

:::{code} python
:caption: Calcul des moyennes mobiles pondérées
:linenos:
import numpy as np

def weighted_rolling_mean(data, weights, window_size=30):
    def weighted_mean(x):
        return np.average(data.loc[x.index], weights=weights.loc[x.index])

    return data.rolling(window_size, min_periods=1).apply(weighted_mean, raw=False)
:::

## Pistes d'améliorations

Voici plusieurs pistes afin d'améliorer et compléter cette étude :
- Ajouter les données manquantes des mandants des entraîneurs sportifs
- Agrandir le cadre d'étude en incluant davantage de saison et de pays
- Améliorer les données sur l'expérience des entraîneurs en incluant des informations sur leur carrière avant 2015
- Observer les causes et conséquences d'un licenciement en cours de saison sur la performance de l'équipe le reste de la saison

## Conclusion

L'analyse des données a permis de mettre en évidence plusieurs corrélations :
- La fréquence de renouvellement des entraîneurs par les clubs est corrélée négativement avec la performance de l'équipe.
- La mobilité des entraîneurs est corrélée positivement avec la performance des équipes entraînées.
- La durée du mandat de l'entraîneur est corrélée positivement avec la performance de l'équipe.

Ces résultats suggèrent que la stabilité et la continuité sont des facteurs importants de la performance sportive d'une équipe. Les entraîneurs qui restent longtemps à la tête de l'équipe ont tendance à mieux connaître les joueurs et à mieux comprendre les forces et les faiblesses de l'équipe, ce qui peut contribuer à améliorer les performances de l'équipe. En revanche, les entraîneurs qui changent régulièrement de club ont tendance à voir une amélioration de la performance de l'équipe. Aussi, les entraîneurs qui changent régulièrement de club semblent acquérir une expérience plus diversifiée qui leur permet d'obtenir de meilleurs résultats.

Cependant, il est difficile de tirer des conclusions définitives sur la causalité de ces relations, car il existe de nombreux autres facteurs qui peuvent influencer la performance d'une équipe de football. Par exemple, la qualité des joueurs, la stratégie de jeu, la gestion du club et d'autres facteurs peuvent également jouer un rôle important dans la performance de l'équipe. Il est donc important de prendre en compte ces facteurs lors de l'analyse des données et de ne pas tirer de conclusions hâtives.

+++ {"part": "data_availability"}
L'ensemble des fichiers et données relatif à ce travail sont disponible en accès libre sur le [dépot GitHub](https://github.com/mathisdrn/head_coach_dismissal) sous licence MIT.
+++