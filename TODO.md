Sujet du TER : Comprendre l'effet du changement de club sur les performances du coach 
ET NON, comme le sujet initial : Comprendre l'effet du changement de coach sur les performances du club
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

To-Do :

- Mettre dans les cellules Markdown les éléments actuellement print à l'aide de eval{}
    - https://myst-nb.readthedocs.io/en/latest/render/inline.html
- Ajouter les figures dans le document paper.md
- Ajouter des tags pour cacher certaines cellules, output ou les deux 
    - https://myst-nb.readthedocs.io/en/latest/render/hiding.html
    - clic droit sur une cellule -> ajouter tag
- Formatter les graphiques
    - https://myst-nb.readthedocs.io/en/latest/render/format_code_cells.html#images-and-figures
- Ajouter les informations de dates au titre des figures
- Présenter les graphiques, expliquer les variables utilisés et ce que permettrait d'interpréter un graphique concluant

- Data extraction : 
    - Présenter les sites où les données ont été extraites
    - Un mot sur la fiabilité des données
- Preprocessing :
    - expliquer le pré-traitement et l'algorithme fuzzy-word + référence au papier
    - déplacer et unifier les partie check de More Preprocessing dans Preprocessing
    - conserver les modifications de données liés à la jointure des deux jeux dans More Preprocessing
    - observer les valeurs nulles, les quantifier, et les supprimer si pertinents
- Headcoach analysis :
    - importance de bien expliquer chacune des régressions et ce qu'elle permettrait de montrer
- Match results : 
    - idem
- More preprocessing :
    - déplacer et unifier dans Preprocessing les checks uniquement
- Statistical analysis :
    - expliquer pourquoi cette regression est celle qui devrait le plus statistiquement la corrélationn : on observe match par match et non à l'échelle de la performance total d'un coach au sein d'une équipe


(Mathis)
- Ajouter les GitHub Action pour page web statique et boutton Launch binder
    https://mystmd.org/guide/deployment
- Ajouter export PDF
    https://mystmd.org/guide/creating-pdf-documents
- Ajuster extending EDA avec le more preprocessing