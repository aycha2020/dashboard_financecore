** FinanceCore SA — Dashboard Streamlit (Multi-pages)
** Contexte du projet

Ce projet consiste à développer un dashboard analytique interactif pour FinanceCore SA, construit avec Streamlit et connecté en temps réel à la base de données PostgreSQL financecore_db via SQLAlchemy.

Le dashboard exploite des données financières nettoyées afin de fournir aux décideurs une vision globale des performances et des risques à travers des visualisations dynamiques et des KPIs métier.

** Objectifs
Connexion à la base de données PostgreSQL via SQLAlchemy
Construction d’un dashboard multi-pages :
** Vue Exécutive
* Analyse des Risques
Calcul et affichage de KPIs financiers clés
Création de visualisations avancées et interactives
Mise en place de filtres dynamiques
Analyse des clients à risque
Export des données filtrées en CSV
Gestion des erreurs et traçabilité (logs)
Documentation et suivi du projet via Jira
 Architecture du Dashboard
🔹 1. Connexion & Préparation des données
Connexion à PostgreSQL avec SQLAlchemy
Requêtes SQL optimisées pour l’analyse
Agrégation des données pour les KPIs et graphiques
* 2. Page 1 — Vue Exécutive

Cette page offre une vision synthétique des performances financières.

** KPIs affichés :
Volume total des transactions
Chiffre d’affaires total (CA)
Nombre de clients actifs
Marge moyenne
** Visualisations :
Courbe d’évolution mensuelle des débits et crédits (2022–2024)
Bar chart : CA par agence et par produit bancaire
Pie chart : répartition des clients par segment :
Premium
Standard
Risqué
* 3. Page 2 — Analyse des Risques

Analyse approfondie du risque client et du comportement financier.

** Visualisations :
Heatmap : corrélation entre :
score crédit
montant des transactions
taux de rejet
Scatter plot :
score crédit vs montant transaction
classification par niveau de risque
** Tableau des risques :
Top 10 des clients les plus à risque
Indicateurs visuels (couleurs / alertes)
* 4. Filtres interactifs

Un panneau latéral permet un filtrage dynamique :

* Agence
* Segment client
* Produit bancaire
* Période (slider années)

* Tous les graphiques et KPIs sont automatiquement mis à jour selon les filtres.

* Export des données
Export des données filtrées en CSV
Permet une exploitation externe (Excel / reporting)
 Stack technique
Python 
Streamlit 
Pandas
SQLAlchemy
PostgreSQL 
Plotly / Matplotlib
** Fonctionnalités clés
Dashboard multi-pages
Visualisations interactives
Analyse des risques avancée
Filtres dynamiques temps réel
Export de données
Architecture scalable et modulaire
** Bonnes pratiques utilisées
Séparation logique des pages Streamlit
Requêtes SQL optimisées
Gestion des erreurs (KeyError, types de données, etc.)
Normalisation des données avant visualisation
** Améliorations futures
Ajout de prédiction de risque (Machine Learning)
Alertes automatiques sur clients à haut risque
Authentification utilisateur
Déploiement cloud (Streamlit Cloud / Docker)
