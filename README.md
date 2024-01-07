# Accélération de l'extraction de règles d'association

## Mots clés

- Analyse formelle de concepts
- Analyse de concepts
- Clustering,
- Data Mining
- K Unified Nearest Neighbor
- Règles d’association
- Système de recommandation

## Objectif

Ce dépôt Git est le résultat d'un projet de recherche mené par 3 étudiants ingénieurs et supervisé par **l'UQAM**, l'université du Québec à Montréal.

La fouille de données est une discipline visant à extraire les tendances et régularités présentes dans les grands jeux de données. On s’intéresse ici à améliorer un processus de fouille de données, l’analyse formelle de concepts, **AFC**, qui permet de générer une base de règles d’associations. En effet, ce processus produit un nombre important de règles dont certaines non nécessaire. 

Afin de l’optimiser, on souhaite appliquer un lissage sur le jeu de données avant d’exécuter l’AFC. Le processus de prétraitement que l’on souhaite utiliser est le k Unified Nearest Neighbor, **kUNN**, un système de recommandation permettant de prédire des valeurs inconnues dans un jeu de donnée binaire.

## Arborescence 

- **data** : contient toutes les données
- **src** : contient tout le code source à l'exception du fichier main
- `main.py` : fichier python à exécuter pour traiter les données initiales, réaliser les calculs et évaluer la précision.
- `research_article.pdf` : article de recherche rédigé par l'équipe d'étudiants. Ce fichier détaille toutes les connaissances mathématique nécessaires à la bonne compréhension du projet ainsi que les choix de conceptions.

## Installation

Après avoir copié le dépôt Git et s'être placé dans le répertoire, on peut exécuter le fichier python main :
```
python main.py
```
Les fichiers **context.csv** et **prediction.csv** sont générés et les résultats de l'algorithme sont retournés. 

# Théorie mathématique

Cette partie se veut volontairement minimaliste pour expliquer l'intérêt du projet et son fonctionnement. Pour plus de détails (les choix de conceptions, les formules utilisés etc), veuillez consulter le fichier `research_article.pdf`.

Prenons une table unaire, c'est-à-dire une table contenant pour chaque élément une valeur ou non. Considérons que les lignes représentent des utilisateurs (**user**) et les colonnes des produits (**item**). L'objectif est de développer un algorithme permettant de recommander à chaque user, une liste d'item susceptible de l'intéresser. Pour ce faire, on développe un système de recommandation que l'on peut diviser en trois grandes étapes :

- **Calcul des similarités** : pour un user donné, calculer le niveau de proximité entre les produits l'intéressant et ceux des autres utilisateurs.
- **Sélection des voisins** : pour un user donné, sélectionner une liste d'autres user jugés comme similaires. On parle de voisin.
- **Calcul des prédictions** : à partir des intérêts des voisins, calculer les items susceptibles d'intéresser le user inital.

Ici, nous avons décrit l'approche user. Mais on peut réaliser la même réflexion via une approche item, c'est à dire en permutant user et item. On propose ainsi de combiner les deux approches pour de meilleurs résultats. 

Pour le calcul des similarités, on utilise la similarité cosinus. Une fois les similarités calculées à la fois pour les users et pour les items, on combine ces deux résultats pour calculer la prédiction.


# Implémentation

### Structure du code

Initialement le dépôt Git ne contient que le fichier **context.cxt**. On propose un premier fichier `parsing.py` traitant ces données pour générer le fichier **context.csv** qui sera utilisé par les autres fichiers python.

On définit ensuite nos métriques pour le calcul des similarités. On choisit la similarités cosinus que l'on va appliquer doublement. On va combiner les points de vue user et item afin d'obtenir de meilleurs résultats. Une fois les classes UserToUser et ItemToItem définit, on construit notre modèle KUNN qui intègre ces deux classes. C'est via notre instance Kunn que l'on va réaliser les calculs de prédictions. Une fois cette tâche terminée, le modèle nous retourne les résultats que l'on va comparer avec le jeu de données. 

### Résultats 

On obtient ainsi les résultats suivants : 
- Réduction du nombre de concepts : 36.93%
- Réduction du nombre de règles d'associations : 75% 
- Précision : 98.95%

