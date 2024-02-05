# -*- coding: utf-8 -*-
"""
Created on Mon May  8 22:23:51 2023

@author: Valen
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

dfx = pd.read_csv("age.csv", delimiter=';')  # Utiliser le fichier Pays.csv comme variables explicatives
dfy = pd.read_csv("votes_12544.csv", delimiter=';')  # Utiliser le fichier votes_1.csv comme variable cible

# Extraire les colonnes en tant que listes
x = dfx.values
y = dfy.values.ravel()  # Ajout de ravel() pour convertir y en tableau 1D

print(x)
print(y)

x_train, x_test, y_train, y_test = \
    train_test_split(x, y, test_size=0.2, random_state=0)
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
model = LogisticRegression(solver='liblinear', C=0.05, random_state=0)
model.fit(x_train, y_train)
LogisticRegression(C=0.05, class_weight=None, dual=False, fit_intercept=True,
                   intercept_scaling=1, l1_ratio=None, max_iter=100,
                   multi_class='auto', n_jobs=None, penalty='l2', random_state=0,
                   solver='liblinear', tol=0.0001, verbose=0, warm_start=False)
x_test = scaler.transform(x_test)
y_pred = model.predict(x_test)

# Évaluation du modèle
print("Classification Report:")
print(classification_report(y_test, y_pred, zero_division=0))  # Ajout de zero_division=0

# Matrice de confusion
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Score de précision
score = model.score(x_test, y_test)
print("Accuracy Score: ", score)

# Charger les données
dfx = pd.read_csv("age.csv", delimiter=';')  # Variables explicatives
dfy = pd.read_csv("votes_12544.csv", delimiter=';')  # Votes des députés

# Extraire les colonnes en tant que listes
x = dfx.values
y = dfy.values.ravel()

# Diviser les données en ensembles d'entraînement et de test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Standardiser les variables explicatives
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# Créer et entraîner le modèle de régression logistique
model = LogisticRegression(solver='liblinear', C=0.05, random_state=0)
model.fit(x_train, y_train)

# Prédire les classes pour les données de test
y_pred = model.predict(x_test)
proba_pred = model.predict_proba(x_test)[:, 1]  # Probabilités de sortie étiquetées comme "1"

# Évaluation du modèle
print("Classification Report:")
print(classification_report(y_test, y_pred, zero_division=0))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
score = model.score(x_test, y_test)
print("Accuracy Score: ", score)

# Tracer les résultats d'entrée, de sortie et de classification
plt.figure(figsize=(8, 6))
plt.scatter(x_test, y_test, color='green', marker='o', label='Réel')
plt.scatter(x_test, y_pred, color='gray', marker='s', label='Prédiction')
plt.scatter(x_test[y_test != y_pred], y_pred[y_test != y_pred], color='red', marker='x', label='Prédiction incorrecte')
plt.plot(x_test, proba_pred, color='black', linestyle='-', label='Ligne de régression logistique')
plt.plot(x_test, np.log(proba_pred / (1 - proba_pred)), color='black', linestyle='--', label='Logit f(x)')
plt.xlabel('Entrée')
plt.ylabel('Sortie')
plt.title('Résultats de la régression logistique')
plt.legend()
plt.show()

"""
# Obtenir les probabilités prédites par le modèle
proba_pred = model.predict_proba(x)[:, 1]  # Probabilités de sortie étiquetées comme "1"

# Tracer les résultats d'entrée, de sortie et de classification
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='green', marker='o', label='Réel')
plt.scatter(x, proba_pred, color='gray', marker='s', label='Probabilité prédite')
plt.scatter(x[y != y_pred], y_pred[y != y_pred], color='red', marker='x', label='Prédiction incorrecte')
plt.plot(x, model.predict_log_proba(x)[:, 1], color='black', linestyle='-', label='Ligne de régression logistique')
plt.plot(x, np.log(proba_pred / (1 - proba_pred)), color='black', linestyle='--', label='Logit f(x)')
plt.xlabel('Entrée')
plt.ylabel('Sortie')
plt.title('Résultats de la régression logistique')
plt.legend()
plt.show()"""

"""liste_pays = ['Poland', 'Bulgaria', 'Italy', 'Malta', 'Spain', 'United Kingdom', 'Sweden', 'France', 'Portugal', 'Latvia', 'Germany', 'Greece', 'Belgium', 'Estonia', 'Hungary', 'Romania', 'Denmark', 'Lithuania', 'Netherlands', 'Slovakia', 'Austria', 'Czech Republic', 'Slovenia', 'Croatia', 'Ireland', 'Cyprus', 'Luxembourg', 'Finland']

# Calculer le nombre de votes "pour" et "contre" pour chaque pays
country_votes_for = {}
country_votes_against = {}
for i, country in enumerate(liste_pays):
    country_votes_for[country] = np.sum(x[y == 1, i])
    country_votes_against[country] = np.sum(x[y == 0, i])

# Trier les pays par nombre de votes "pour"
sorted_countries_for = sorted(country_votes_for.items(), key=lambda x: x[1], reverse=True)

# Extraire les noms des pays et les nombres de votes "pour"
sorted_country_names_for = [item[0] for item in sorted_countries_for]
sorted_vote_counts_for = [item[1] for item in sorted_countries_for]

# Trier les pays par nombre de votes "contre"
sorted_countries_against = sorted(country_votes_against.items(), key=lambda x: x[1], reverse=True)

# Extraire les noms des pays et les nombres de votes "contre"
sorted_country_names_against = [item[0] for item in sorted_countries_against]
sorted_vote_counts_against = [item[1] for item in sorted_countries_against]

# Créer un graphique à barres pour les votes "pour" et "contre"
plt.figure(figsize=(12, 6))
bar_width = 0.35
index = np.arange(len(liste_pays))

plt.bar(index, sorted_vote_counts_for, bar_width, label='Pour')
plt.bar(index + bar_width, sorted_vote_counts_against, bar_width, label='Reste')

plt.xlabel('Pays')
plt.ylabel('Nombre de votes')
plt.title('Tendance des votes "pour" et "contre" pour chaque pays')
plt.xticks(index + bar_width / 2, sorted_country_names_for, rotation=90)
plt.legend()
plt.tight_layout()
plt.show()"""
"""
# Extraire les probabilités pour la classe "pour" et "contre"
y_pred_prob = model.predict_proba(x_test)
proba_pour = y_pred_prob[:, 1]
proba_contre = y_pred_prob[:, 0]

# Tracer l'histogramme des probabilités prédites
plt.figure(figsize=(8, 6))
plt.hist(proba_pour, bins=20, alpha=0.5, label='Pour')
plt.hist(proba_contre, bins=20, alpha=0.5, label='Contre')
plt.xlabel('Probabilité')
plt.ylabel('Fréquence')
plt.title('Histogramme des probabilités prédites')
plt.legend()
plt.show()"""