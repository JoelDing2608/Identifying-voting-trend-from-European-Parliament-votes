# -*- coding: utf-8 -*-
"""
Created on Tue May  9 08:57:48 2023
@author: Valentin
"""
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.feature_selection import RFECV

# Charger les données
dfx_country = pd.read_csv("indice_country.csv", delimiter=';')
dfx_party = pd.read_csv("indice_party.csv", delimiter=';',encoding = 'latin-1')
dfx_epg = pd.read_csv("indice_epg.csv", delimiter=';')
dfx_age =  pd.read_csv("age.csv", delimiter=';')
dfy = pd.read_csv("votes_12546.csv", delimiter=';')

# Fusionner les données des différents tableaux
dfx = pd.concat([dfx_country, dfx_party, dfx_epg, dfx_age], axis=1)
print(dfx)
# Extraire les colonnes en tant que tableau
x = dfx.values
y = dfy.values.ravel()
print(len(y))
print(len(x))

# Fractionner les données en ensembles d'entraînement et de test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Standardiser les données
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# Créer et entraîner le modèle de régression logistique
model = LogisticRegression(solver='liblinear', random_state=0)
model.fit(x_train, y_train)

# Prédire les votes à partir des données de test
y_pred = model.predict(x_test)
"""
# Évaluation du modèle
print("Score de précision :", model.score(x_test, y_test))

# Matrice de confusion
confusion = confusion_matrix(y_test, y_pred)
print("Matrice de confusion :")
print(confusion)

# Rapport de classification
classification = classification_report(y_test, y_pred)
print("Rapport de classification :")
print(classification)
"""
# Récupérer les coefficients de régression spécifiques à chaque variable
coeff_country = model.coef_[0][:dfx_country.shape[1]]
coeff_party = model.coef_[0][dfx_country.shape[1]:dfx_country.shape[1] + dfx_party.shape[1]]
coeff_epg = model.coef_[0][dfx_country.shape[1] + dfx_party.shape[1]:dfx_country.shape[1] + dfx_party.shape[1] + dfx_epg.shape[1]]
coeff_ages = model.coef_[0][dfx_country.shape[1] + dfx_party.shape[1] + dfx_epg.shape[1]:]

#coeff_party = model.coef_[0][dfx_country.shape[1]:dfx_country.shape[1] + dfx_party.shape[1]]
#coeff_epg = model.coef_[0][dfx_country.shape[1] + dfx_party.shape[1]:]

# Tracer le graphique des coefficients de régression pour les pays
countries = ['Poland', 'Bulgaria', 'Italy', 'Malta', 'Spain', 'United Kingdom', 'Sweden', 'France', 'Portugal', 'Latvia', 'Germany', 'Greece', 'Belgium', 'Estonia', 'Hungary', 'Romania', 'Denmark', 'Lithuania', 'Netherlands', 'Slovakia', 'Austria', 'Czech Republic', 'Slovenia', 'Croatia', 'Ireland', 'Cyprus', 'Luxembourg', 'Finland']
ages=["20_25","25_30","30_35","35_40","40_45","45_50","50_55","55_60","60_65","65_70","70_75","75_80","80_85","85_90","Autre"]
parties=['Independent', 'Citizens for European Development of Bulgaria', 'Forza Italia', 'Lega', 'Partit Laburista', 'Vox', 'Partido Socialista Obrero Espaï¿½ï', 'Green Party', 'Centerpartiet', 'Union of Democratic Forces', 'Rï¿½ï¿½gions et Peuples Solida', 'Movement for Rights and Freedoms', 'Scottish National Party', 'Partido Social Democrata', 'Gods kalpot Rï¿½ï¿', 'Alternative fï¿½ï¿½r Deutsch', 'Sinn Fï¿½ï', 'Bï¿½ï¿½ndnis 90/Die Grï', 'Parti Socialiste', 'Rassemblement national', 'PASOK-KINAL', 'Vlaams Belang', 'Eesti Reformierakond', 'Demokratikus Koalï¿½ï¿½', 'Partido Popular', 'Christlich Soziale Partei', 'Platforma Obywatelska', 'Uniunea Salvaï¿½ï¿½i Romï', 'Coalition of the Radical Left', 'Nea Demokratia', 'La France Insoumise', 'Socialistisk Folkeparti', 'Lietuvos Respublikos liberalï¿½ï¿½ sï¿½ï', 'Partidul Social Democrat', 'Volkspartij voor Vrijheid en Democratie', '', 'Sozialdemokratische Partei Deutschlands', 'EH BILDU', 'Partito Democratico', 'Partidul Miï¿½ï¿½carea Popul', 'Ciudadanos ï¿½ï¿½ï¿½ Partido de la Ciuda', 'Liberal Democrats', 'Freie Demokratische Partei', 'Movimento 5 Stelle', 'Les Rï¿½ï¿½public', 'SMER-Sociï¿½ï¿½lna demokr', 'Christlich Demokratische Union Deutschlands', 'Christen Democratisch Appï¿½', 'Liberal-Conservative Refomists', 'Arbetarepartiet- Socialdemokraterna', 'ýýsterreichische Volkspartei', 'La Rï¿½ï¿½publique en ma', 'Partido Nacionalista Vasco', 'SPOLU ï¿½ï¿½ï¿½ obï¿½ï¿½ianska ', 'Europe ï¿½ï¿½col', 'Vï¿½ï¿½nsterpar', 'Partidul Naï¿½ï¿½ional Lib', 'Svoboda a pï¿½ï¿½ï¿½ï¿½mï¿½ï¿', 'Lietuvos socialdemokratï¿½ï¿½ par', 'Fidesz-Magyar Polgï¿½ï¿½ri Szï¿½ï¿½vetsï¿½ï¿½g-Keresztï¿½ï¿½nydem', 'Volt', 'Slovenska ljudska stranka', 'Socijaldemokratska partija Hrvatske', 'Parti du Travail de Belgique', 'Nieuw-Vlaamse Alliantie', 'Piratenpartei Deutschland', 'Socialni demokrati', "Ecologistes Confï¿½ï¿½dï¿½ï¿½rï¿½ï¿½s pour l'Organisation de Lutte", 'Prawo i Sprawiedliwoï¿½ï', 'Mouvement Dï¿½ï¿½moc', 'ýýkologisch-Demokratische Partei', 'The Brexit Party', 'Azione', 'Liste Renaissance', 'Partido Socialista', 'Partit Nazzjonalista', 'Partij van de Arbeid', 'Ano 2011', 'Mouvement Rï¿½ï¿½forma', 'Venstre, Danmarks Liberale Parti', 'Democratic Rally', 'Sojusz Lewicy Demokratycznej - Unia Pracy', 'Les centristes', 'Labour Party', 'PRO Romania', 'Momentum', 'ChristenUnie', 'Independents for change', 'DIE LINKE.', 'Groen', 'Democratic Unionist Party', 'Christlich-Soziale Union in Bayern e.V.', 'Sï¿½ï¿½dtiroler Volkspa', 'VMRO', 'GroenLinks', 'JA21', 'Freie Wï¿½ï¿½', 'Plaid Cymru - Party of Wales', 'Europa Verde', 'Partido Comunista Portuguï¿½', "Fratelli d'Italia", 'Fine Gael Party', 'Istarski demokratski sabor - Dieta democratica istriana', 'Elliniki Lusi-Greek Solution', 'Christen-Democratisch & Vlaams', 'Socialdemokratiet', 'NEOS ï¿½ï¿½ï¿½ Das Neue ï¿½ï¿', 'Progressive Party of Working People - Left - New Forces', 'Familien-Partei Deutschlands', 'USR-PLUS', 'Place publique', 'Parti dï¿½ï¿½mocrat', 'Partidul Puterii Umaniste', 'PIRï¿½ï', 'Lista Marjana ï¿½ï¿½', 'Independente', 'Bloco de Esquerda', 'JOBBIK MAGYARORSZï¿½ï¿½Gï¿½ï¿½RT ', 'Freiheitliche Partei ï¿½ï¿½sterre', 'Perussuomalaiset', 'Conservative Party', 'Parti chrï¿½ï¿½tien social luxembourg', 'Vihreï¿½ï¿½ li', 'Partij voor de Dieren', 'Sozialdemokratische Partei ï¿½ï¿½sterre', 'Suomen Sosialidemokraattinen Puolue/Finlands Socialdemokratiska Parti', 'Polskie Stronnictwo Ludowe', 'Progresï¿½ï¿½vne Slove', 'Miljï¿½ï¿½partiet de gr', 'Bulgarian Socialist Party', 'Attï¿½ï¿½stï¿½ï¿½', 'Democraten 66', 'Solidarna Polska Zbigniewa Ziobro', 'Tï¿½ï¿½vynï¿½ï¿½s sï¿½ï¿½junga-Lietuvos krikï¿½ï¿½ï¿', 'Sloboda a Solidarita', 'Panhellenic Socialist Movement - Olive Tree', 'Sotsiaaldemokraatlik Erakond', "Partija 'VIENOTï¿½ï¿", 'Democrats for Strong Bulgaria', 'Liberalerna', 'Suomen Keskusta', 'Fianna Fï¿½ï¿½il P', 'Agir - La Droite constructive', 'Dansk Folkeparti', 'Moderaterna', '-', 'Komunistickï¿½ï¿½ strana ï¿½ï¿½ech ', 'Nouvelle Donne', 'Kristdemokraterna', 'Alliance Party of Northern Ireland', 'Partit dels Socialistes de Catalunya', 'Sverigedemokraterna', 'Eesti Konservatiivne Rahvaerakond', 'Gauche rï¿½ï¿½publicaine et social', 'Democratic Party', "Nacionï¿½ï¿½lï¿½ï¿½ apvienï¿½ï¿½ba 'Visu Latvijai!'-'Tï¿½ï¿½vzemei un ", 'Det Radikale Venstre', 'Partido do Centro Democrï¿½ï¿½tico Social-Partido Pop', 'Dï¿½ï¿½i Grï¿½ï¿½ng - L', 'Vasemmistoliitto', 'Independiente', 'TOP 09 a Starostovï¿', 'Communist Party of Greece', 'Nova Slovenija ï¿½ï¿½ï¿½ Krï¿½ï¿½ï¿½ï¿½a', 'Delegaciï¿½ï¿½n Ciudadanos Euro', 'Movement for Social Democracy EDEK', 'Kansallinen Kokoomus', 'Izquierda Unida', 'Starostovï¿½ï¿½ a nezï¿½', 'Obyï¿½ï¿½ajnï¿½ï¿½ ï¿½ï¿½udia a nezï¿½ï¿½', 'Slovak PATRIOT', 'Hrvatska demokratska zajednica', 'Esquerra Republicana de Catalunya', 'Mouvement Radical Social-Libï¿½ï¿', 'PODEMOS', 'Lietuvos valstieï¿½ï¿½iï¿½ï¿½ ir ï¿½ï¿½aliï¿', 'Staatkundig Gereformeerde Partij', 'Parti ouvrier socialiste luxembourgeois', 'Indï¿½ï¿½pen', 'ýýivi Zid', 'Kï¿½ï¿½esï¿½ï¿½anskï¿½ï¿½ a demokratickï¿½ï¿½ unie - ï¿½ï¿½eskoslove', 'Die PARTEI', 'Kresï¿½ï¿½anskodemokratickï¿½ï¿', 'Partidul Naï¿½ï¿½ional ï¿½ï¿½aranesc Creï¿½ï¿½', 'Lietuvos lenkï¿½ï¿½ rinkimï¿½ï¿½ akcija ï¿½ï¿½ï¿½ Krikï¿½ï¿½ï¿½ï¿½ioni', 'Hrvatska konzervativna stranka', 'Slovenska demokratska stranka', 'Eesti Keskerakond', 'Svenska folkpartiet', 'Obï¿½ï¿½anskï¿½ï¿½ demokratickï', 'Hnutie Republika', 'Magyar Szocialista Pï¿½ï', 'ANTICAPITALISTAS', 'Catalunya en Comï¿', "'Saskaï¿½ï¿½a' sociï¿½ï¿½ldemokrï¿½ï¿½ti", 'Darbo partija', 'Die Grï¿½ï¿½nen - Die Grï¿½ï¿½ne Alt', 'Socialistische Partij.Anders', 'Open Vlaamse Liberalen en Democraten', 'Enhedslisten', 'Uniunea Democratï¿½ï¿½ Maghiarï¿½ï¿½ din ', 'Det Konservative Folkeparti', 'Latvijas Krievu savienï¿½ï', 'Italia Viva', 'Junts per Catalunya - Lliures per Europa', 'Isamaa', 'Partij voor de Vrijheid']
epgs=['EPP', 'IDG', 'S&D', 'ECR', 'Greens/EFA', 'REG', '', 'The Left', 'NI']
# Tracer le graphique des coefficients de régression pour les pays
plt.figure(figsize=(10,5))
plt.bar(countries, coeff_country,color='orange')
plt.title("Coefficients de régression pour les pays")
plt.xticks(rotation=90)
plt.show()

# Tracer le graphique des coefficients de régression pour les parties
plt.figure(figsize=(60,5))
plt.bar(parties, coeff_party,color='orange')
plt.title("Coefficients de régression pour les parties")
plt.xticks(rotation=90)
plt.show()

# Tracer le graphique des coefficients de régression pour epgs
plt.figure(figsize=(10,5))
plt.bar(epgs, coeff_epg,color='orange')
plt.title("Coefficients de régression pour epgs")
plt.xticks(rotation=90)
plt.show()

# Tracer le graphique des coefficients de régression pour les âges
plt.figure(figsize=(10,5))
plt.bar(ages, coeff_ages,color='orange')
plt.title("Coefficients de régression pour les âges")
plt.xticks(rotation=90)
plt.show()






# Créer le sélecteur RFE
selector = RFECV(estimator=model, step=1, cv=5)

# Adapter le sélecteur aux données
selector.fit(x_train, y_train)

# Transformer les données d'entraînement
x_train_selected = selector.transform(x_train)
x_test_selected = selector.transform(x_test)

# Entraîner un nouveau modèle sur les caractéristiques sélectionnées
model_selected = LogisticRegression(solver='liblinear', random_state=0)
model_selected.fit(x_train_selected, y_train)

# Prédire les votes à partir des données de test sélectionnées
y_pred_selected = model_selected.predict(x_test_selected)

# Évaluation du modèle
print("Score de précision après sélection de variables :", model_selected.score(x_test_selected, y_test))

# Matrice de confusion
confusion_selected = confusion_matrix(y_test, y_pred_selected)
print("Matrice de confusion après sélection de variables :")
print(confusion_selected)

# Rapport de classification
classification_selected = classification_report(y_test, y_pred_selected)
print("Rapport de classification après sélection de variables :")
print(classification_selected)






"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix

# Charger les données
dfx_country = pd.read_csv("indice_country.csv", delimiter=';')
dfx_party = pd.read_csv("indice_party.csv", delimiter=';',encoding = 'latin-1')
dfx_epg = pd.read_csv("indice_epg.csv", delimiter=';')
dfx_age =  pd.read_csv("age.csv", delimiter=';')
dfy = pd.read_csv("votes_12546.csv", delimiter=';')

# Fusionner les données des différents tableaux
dfx = pd.concat([dfx_country, dfx_party, dfx_epg, dfx_age], axis=1)

# Extraire les colonnes en tant que tableau
x = dfx.values
y = dfy.values.ravel()

# Fractionner les données en ensembles d'entraînement et de test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Standardiser les données
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# Créer et entraîner le modèle de régression logistique
model = LogisticRegression(solver='liblinear', random_state=0)
model.fit(x_train, y_train)

# Prédire les votes à partir des données de test
y_pred = model.predict(x_test)

# Calcul des probabilités prédites
y_pred_prob = model.predict_proba(x_test)[:, 1]

# Création du dataframe pour le test de Hosmer-Lemeshow
df_hl = pd.DataFrame({'y': y_test, 'y_pred_prob': y_pred_prob})

# Diviser les observations en groupes de probabilités prédites (déciles)
df_hl['decile'] = pd.qcut(df_hl['y_pred_prob'], 10, labels=False)

# Calcul des statistiques pour le test de Hosmer-Lemeshow
df_hl['event'] = df_hl['y']
df_hl['nonevent'] = 1 - df_hl['y']
df_hl['event_predicted'] = df_hl['y_pred_prob']
df_hl['nonevent_predicted'] = 1 - df_hl['y_pred_prob']

# Calcul des sommes cumulées
df_hl_cumsum = df_hl.groupby('decile').sum()

# Calcul des proportions cumulées
df_hl_cumsum['event_cumsum'] = df_hl_cumsum['event'].cumsum()
df_hl_cumsum['nonevent_cumsum'] = df_hl_cumsum['nonevent'].cumsum()
df_hl_cumsum['event_predicted_cumsum'] = df_hl_cumsum['event_predicted'].cumsum()
df_hl_cumsum['nonevent_predicted_cumsum'] = df_hl_cumsum['nonevent_predicted'].cumsum()

# Calcul des proportions de succès et d'échecs prédits
df_hl_cumsum['event_predicted_prop'] = df_hl_cumsum['event_predicted_cumsum'] / df_hl_cumsum['event_predicted_cumsum'].sum()
df_hl_cumsum['nonevent_predicted_prop'] = df_hl_cumsum['nonevent_predicted_cumsum'] / df_hl_cumsum['nonevent_predicted_cumsum'].sum()

# Calcul des proportions de succès et d'échecs observés
df_hl_cumsum['event_prop'] = df_hl_cumsum['event_cumsum'] / df_hl_cumsum['event_cumsum'].sum()
df_hl_cumsum['nonevent_prop'] = df_hl_cumsum['nonevent_cumsum'] / df_hl_cumsum['nonevent_cumsum'].sum()

# Calcul de la statistique de Hosmer-Lemeshow
df_hl_cumsum['HL_stat'] = (df_hl_cumsum['event_prop'] - df_hl_cumsum['event_predicted_prop']) ** 2 / df_hl_cumsum['event_predicted_prop'] + (df_hl_cumsum['nonevent_prop'] - df_hl_cumsum['nonevent_predicted_prop']) ** 2 / df_hl_cumsum['nonevent_predicted_prop']
HL_statistic = df_hl_cumsum['HL_stat'].sum()

# Calcul du degré de liberté
df_hl_cumsum['group_size'] = df_hl_cumsum['event_cumsum'] + df_hl_cumsum['nonevent_cumsum']
df_hl_cumsum['expected_events'] = df_hl_cumsum['event_predicted_cumsum'].sum() * df_hl_cumsum['group_size'] / df_hl_cumsum['group_size'].sum()
df_hl_cumsum['df'] = df_hl_cumsum['group_size'] - 2

# Affichage des résultats
print("Statistique de Hosmer-Lemeshow :", HL_statistic)
print("Degré de liberté :", df_hl_cumsum['df'].sum())
import matplotlib.pyplot as plt

# Calcul des proportions de succès observées et prédites
df_hl_cumsum['event_observed_prop'] = df_hl_cumsum['event_cumsum'] / df_hl_cumsum['group_size']
df_hl_cumsum['event_predicted_prop'] = df_hl_cumsum['event_predicted_cumsum'] / df_hl_cumsum['group_size']

# Tracé de la courbe de calibration
plt.plot(df_hl_cumsum['event_predicted_prop'], df_hl_cumsum['event_observed_prop'], marker='o')
plt.plot([0, 1], [0, 1], linestyle='--', color='gray')
plt.xlabel('Proportion de succès prédite')
plt.ylabel('Proportion de succès observée')
plt.title('Courbe de calibration')
plt.show()
"""
