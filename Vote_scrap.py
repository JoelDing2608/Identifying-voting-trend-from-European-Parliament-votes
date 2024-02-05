import pandas as pd
import numpy as np

df = pd.read_excel("EP9_RCVs_2022_06_22.xlsx")
# Extraire les colonnes en tant que listes
liste_party = df['Party'].tolist()
liste_epg = df['EPG'].tolist()
liste_country = df['Country'].tolist()
countries=pd.unique(pd.Series(liste_country))
epg = pd.unique(pd.Series(liste_epg))
party = pd.unique(pd.Series(liste_party))
liste_result_votes = df['VOTE2'].tolist()    

for i in range(0, len(liste_result_votes)):
    if liste_result_votes[i] != 1:
        liste_result_votes[i] = 0
votes = [0, 1]

#print(votes)

indice_votes = np.array(liste_result_votes)
indice_votes = indice_votes.T

fmt = "%d"
np.savetxt('votes_12546.csv', indice_votes, delimiter=".", fmt = fmt)



"""
print(countries)
print(party)
print(epg)


countries = ['Poland', 'Bulgaria', 'Italy', 'Malta', 'Spain', 'United Kingdom', 'Sweden', 'France', 'Portugal', 'Latvia', 'Germany', 'Greece', 'Belgium', 'Estonia', 'Hungary', 'Romania', 'Denmark', 'Lithuania', 'Netherlands', 'Slovakia', 'Austria', 'Czech Republic', 'Slovenia', 'Croatia', 'Ireland', 'Cyprus', 'Luxembourg', 'Finland']

listecountry = ['Poland', 'Bulgaria', 'Italy', 'Italy', 'Malta', 'Spain', 'Spain', 'United Kingdom', 'Sweden', 'Bulgaria', 'France', 'Bulgaria', 'United Kingdom', 'Portugal', 'Latvia', 'Germany', 'United Kingdom', 'Germany', 'France', 'France', 'Greece', 'Belgium', 'Estonia', 'Hungary', 'Belgium', 'Spain', 'Belgium', 'Poland', 'Romania', 'Greece', 'Greece', 'France', 'Denmark', 'Lithuania', 'Romania', 'Netherlands', 'Italy', 'Poland', 'France', 'Germany', 'Spain', 'Italy', 'Romania', 'Italy', 'Spain', 'France', 'United Kingdom', 'Germany', 'Germany', 'Italy', 'France', 'Poland', 'France', 'Romania', 'Italy', 'Spain', 'United Kingdom', 'Slovakia', 'Germany', 'Netherlands', 'Germany', 'Germany', 'Sweden', 'Italy', 'Austria', 'Poland', 'Poland', 'France', 'Spain', 'Slovakia', 'France', 'Germany', 'France', 'Italy', 'Sweden', 'Romania', 'Czech Republic', 'Lithuania', 'Germany', 'Hungary', 'Germany', 'Romania', 'Slovenia', 'France', 'Italy', 'Italy', 'Italy', 'Croatia', 'Belgium', 'Romania', 'Belgium', 'France', 'Germany', 'Slovenia', 'Belgium', 'United Kingdom', 'Poland', 'France', 'France', 'Germany', 'Germany', 'Romania', 'United Kingdom', 'Germany', 'United Kingdom', 'United Kingdom', 'Germany', 'Germany', 'Romania', 'Germany', 'Spain', 'Poland', 'Italy', 'Italy', 'Spain', 'France', 'France', 'Italy', 'Ireland', 'Portugal', 'Portugal', 'Malta', 'Italy', 'Germany', 'Italy', 'Spain', 'Germany', 'Italy', 'Portugal', 'France', 'Netherlands', 'France', 'Czech Republic', 'Belgium', 'Italy', 'United Kingdom', 'Denmark', 'Cyprus', 'Poland', 'Italy', 'Romania', 'Romania', 'Slovakia', 'France', 'France', 'Italy', 'United Kingdom', 'France', 'Italy', 'Italy', 'Romania', 'Hungary', 'Ireland', 'Malta', 'Poland', 'Netherlands', 'Malta', 'Ireland', 'Italy', 'United Kingdom', 'Sweden', 'France', 'Italy', 'United Kingdom', 'Czech Republic', 'United Kingdom', 'Italy', 'France', 'France', 'Hungary', 'France', 'United Kingdom', 'Belgium', 'Germany', 'Germany', 'Belgium', 'Hungary', 'United Kingdom', 'France', 'Portugal', 'Czech Republic', 'Hungary', 'United Kingdom', 'Germany', 'Hungary', 'Italy', 'Italy', 'United Kingdom', 'Italy', 'Poland', 'Germany', 'Spain', 'France', 'Slovakia', 'Bulgaria', 'Austria', 'Germany', 'Netherlands', 'United Kingdom', 'Netherlands', 'Germany', 'Germany', 'Germany', 'Spain', 'United Kingdom', 'Italy', 'France', 'Slovenia', 'Romania', 'United Kingdom', 'France', 'Sweden', 'Germany', 'Portugal', 'Spain', 'Italy', 'Italy', 'Portugal', 'Germany', 'Italy', 'Italy', 'Italy', 'Ireland', 'Ireland', 'Croatia', 'United Kingdom', 'Poland', 'Cyprus', 'United Kingdom', 'Greece', 'Poland', 'Belgium', 'Germany', 'Germany', 'Sweden', 'Denmark', 'Italy', 'Denmark', 'Germany', 'Hungary', 'Spain', 'Austria', 'Italy', 'Spain', 'Spain', 'Spain', 'Spain', 'Spain', 'Spain', 'France', 'Germany', 'Germany', 'Germany', 'Italy', 'Cyprus', 'Greece', 'Germany', 'Romania', 'Italy', 'United Kingdom', 'Germany', 'Germany', 'United Kingdom', 'United Kingdom', 'United Kingdom', 'Germany', 'France', 'Luxembourg', 'Spain', 'Spain', 'Spain', 'Italy', 'Romania', 'Czech Republic', 'United Kingdom', 'France', 'Slovenia', 'France', 'Italy', 'Italy', 'Portugal', 'France', 'France', 'Portugal', 'Sweden', 'Hungary', 'Hungary', 'Hungary', 'United Kingdom', 'Germany', 'Germany', 'Austria', 'Slovakia', 'Finland', 'Poland', 'United Kingdom', 'Luxembourg', 'United Kingdom', 'Germany', 'Finland', 'Romania', 'France', 'Netherlands', 'United Kingdom', 'Austria', 'Finland', 'Germany', 'Germany', 'Poland', 'Hungary', 'Czech Republic', 'Germany', 'Slovakia', 'Sweden', 'Hungary', 'Spain', 'United Kingdom', 'France', 'United Kingdom', 'United Kingdom', 'Bulgaria', 'Poland', 'Finland', 'Netherlands', 'Latvia', 'Sweden', 'Netherlands', 'France', 'Germany', 'Lithuania', 'Poland', 'France', 'France', 'Hungary', 'Poland', 'United Kingdom', 'Netherlands', 'United Kingdom', 'France', 'Slovenia', 'Lithuania', 'Poland', 'Slovakia', 'France', 'Greece', 'Poland', 'Estonia', 'Latvia', 'Germany', 'Bulgaria', 'Belgium', 'Austria', 'France', 'Sweden', 'Poland', 'Finland', 'Greece', 'Ireland', 'France', 'Germany', 'Ireland', 'Poland', 'United Kingdom', 'Cyprus', 'Poland', 'Czech Republic', 'Denmark', 'Denmark', 'Poland', 'Sweden', 'Greece', 'Czech Republic', 'Croatia', 'Czech Republic', 'Greece', 'Poland', 'Poland', 'Germany', 'Hungary', 'Germany', 'Greece', 'Greece', 'Czech Republic', 'Bulgaria', 'Germany', 'Poland', 'Germany', 'Poland', 'Lithuania', 'Sweden', 'Germany', 'Finland', 'Poland', 'Greece', 'Greece', 'Bulgaria', 'Germany', 'Greece', 'France', 'Belgium', 'Italy', 'Germany', 'Netherlands', 'Germany', 'France', 'France', 'France', 'France', 'Sweden', 'Poland', 'Portugal', 'Netherlands', 'Poland', 'Poland', 'Germany', 'Germany', 'Germany', 'Italy', 'France', 'Denmark', 'United Kingdom', 'United Kingdom', 'Spain', 'Spain', 'Spain', 'Spain', 'United Kingdom', 'Spain', 'Poland', 'Sweden', 'Belgium', 'Germany', 'Ireland', 'United Kingdom', 'United Kingdom', 'Estonia', 'Spain', 'United Kingdom', 'Italy', 'Lithuania', 'Spain', 'Romania', 'Netherlands', 'Austria', 'France', 'Romania', 'Germany', 'Portugal', 'Portugal', 'Italy', 'Portugal', 'Croatia', 'France', 'Cyprus', 'Czech Republic', 'Bulgaria', 'Austria', 'Poland', 'Lithuania', 'Greece', 'Latvia', 'Denmark', 'France', 'Portugal', 'Malta', 'Luxembourg', 'Germany', 'Germany', 'Bulgaria', 'Estonia', 'Italy', 'Spain', 'Poland', 'United Kingdom', 'Finland', 'United Kingdom', 'Hungary', 'Portugal', 'United Kingdom', 'Spain', 'United Kingdom', 'France', 'Spain', 'Italy', 'Germany', 'Romania', 'Poland', 'Germany', 'United Kingdom', 'Romania', 'Netherlands', 'Spain', 'United Kingdom', 'Germany', 'Germany', 'United Kingdom', 'Romania', 'Germany', 'Czech Republic', 'Germany', 'Finland', 'Greece', 'Germany', 'Slovenia', 'Bulgaria', 'Ireland', 'Poland', 'Germany', 'Poland', 'Lithuania', 'France', 'France', 'United Kingdom', 'Estonia', 'Spain', 'United Kingdom', 'Italy', 'Cyprus', 'Greece', 'Greece', 'Italy', 'United Kingdom', 'Germany', 'Italy', 'Belgium', 'Finland', 'Czech Republic', 'France', 'Bulgaria', 'Portugal', 'Portugal', 'Denmark', 'Denmark', 'United Kingdom', 'United Kingdom', 'Italy', 'Croatia', 'Germany', 'Finland', 'Italy', 'Spain', 'France', 'Netherlands', 'Italy', 'Romania', 'Portugal', 'Romania', 'Czech Republic', 'Sweden', 'Slovakia', 'Poland', 'United Kingdom', 'Czech Republic', 'Italy', 'United Kingdom', 'Slovakia', 'Bulgaria', 'Germany', 'Netherlands', 'Poland', 'Portugal', 'United Kingdom', 'Italy', 'Austria', 'Spain', 'Germany', 'Germany', 'Croatia', 'Spain', 'Belgium', 'Italy', 'France', 'United Kingdom', 'France', 'France', 'Italy', 'Spain', 'Spain', 'Spain', 'Hungary', 'Italy', 'Netherlands', 'Netherlands', 'France', 'Lithuania', 'France', 'United Kingdom', 'United Kingdom', 'Netherlands', 'Spain', 'Poland', 'Italy', 'Spain', 'France', 'Malta', 'Portugal', 'Italy', 'Finland', 'Poland', 'Italy', 'France', 'Denmark', 'Austria', 'Germany', 'Austria', 'Luxembourg', 'Germany', 'Germany', 'Netherlands', 'Netherlands', 'Germany', 'Germany', 'Germany', 'United Kingdom', 'Germany', 'France', 'Luxembourg', 'Germany', 'Austria', 'Poland', 'Portugal', 'Slovakia', 'Germany', 'Croatia', 'Germany', 'Sweden', 'Bulgaria', 'Italy', 'United Kingdom', 'Czech Republic', 'Croatia', 'Spain', 'Germany', 'Poland', 'Greece', 'Italy', 'Bulgaria', 'United Kingdom', 'Slovakia', 'Romania', 'Sweden', 'Netherlands', 'Romania', 'Croatia', 'Hungary', 'Poland', 'Italy', 'Netherlands', 'Belgium', 'Italy', 'Netherlands', 'United Kingdom', 'Romania', 'Spain', 'Austria', 'Poland', 'United Kingdom', 'Netherlands', 'Italy', 'Sweden', 'Poland', 'Italy', 'France', 'Romania', 'Lithuania', 'Croatia', 'Slovenia', 'Estonia', 'Finland', 'Czech Republic', 'Hungary', 'France', 'Italy', 'France', 'Hungary', 'Romania', 'Romania', 'Slovakia', 'Hungary', 'Spain', 'Spain', 'Latvia', 'Lithuania', 'Latvia', 'Romania', 'Austria', 'Belgium', 'Belgium', 'United Kingdom', 'Belgium', 'Netherlands', 'Belgium', 'France', 'Greece', 'Germany', 'Belgium', 'Austria', 'Spain', 'Denmark', 'Romania', 'Denmark', 'Finland', 'Bulgaria', 'United Kingdom', 'Austria', 'Germany', 'Czech Republic', 'United Kingdom', 'Germany', 'Greece', 'Czech Republic', 'Italy', 'Ireland', 'Ireland', 'Germany', 'Sweden', 'United Kingdom', 'Poland', 'Germany', 'Sweden', 'Denmark', 'United Kingdom', 'United Kingdom', 'Germany', 'Austria', 'Slovakia', 'Romania', 'Austria', 'Luxembourg', 'Poland', 'Germany', 'Netherlands', 'France', 'France', 'Bulgaria', 'France', 'Greece', 'Czech Republic', 'Poland', 'Italy', 'Italy', 'Spain', 'Latvia', 'Czech Republic', 'Latvia', 'Germany', 'Poland', 'Spain', 'Portugal', 'Croatia', 'Italy', 'Slovenia', 'Italy', 'Luxembourg', 'Spain', 'Croatia', 'Romania', 'Spain', 'Spain', 'Finland', 'United Kingdom', 'Ireland', 'Italy', 'France', 'Ireland', 'Sweden', 'Spain', 'Italy', 'France', 'France', 'Croatia', 'France', 'Slovakia', 'Spain', 'France', 'Romania', 'Spain', 'Spain', 'Austria', 'Italy', 'Denmark', 'Poland', 'Estonia', 'Spain', 'Netherlands', 'Netherlands', 'Netherlands', 'Austria', 'Ireland', 'Germany', 'Spain', 'Belgium', 'Malta', 'Romania', 'Ireland', 'Romania', 'Hungary', 'Belgium', 'Sweden', 'Netherlands', 'Netherlands', 'Croatia', 'Portugal', 'Germany', 'Sweden', 'Germany', 'Germany', 'Netherlands', 'Italy', 'Germany', 'Slovenia']

epg = ['EPP', 'IDG', 'S&D', 'ECR', 'Greens/EFA', 'REG', '', 'The Left', 'NI']

party = ['Independent', 'Citizens for European Development of Bulgaria',
 'Forza Italia', 'Lega', 'Partit Laburista', 'Vox',
 'Partido Socialista Obrero Español', 'Green Party', 'Centerpartiet',
 'Union of Democratic Forces', 'Régions et Peuples Solidaires',
 'Movement for Rights and Freedoms', 'Scottish National Party',
 'Partido Social Democrata', 'Gods kalpot Rīgai',
 'Alternative für Deutschland', 'Sinn Féin', 'Bündnis 90/Die Grünen',
 'Parti Socialiste', 'Rassemblement national', 'PASOK-KINAL', 'Vlaams Belang',
 'Eesti Reformierakond', 'Demokratikus Koalíció', 'Partido Popular',
 'Christlich Soziale Partei', 'Platforma Obywatelska',
 'Uniunea Salvați România', 'Coalition of the Radical Left',
 'Nea Demokratia', 'La France Insoumise', 'Socialistisk Folkeparti',
 'Lietuvos Respublikos liberalų sąjūdis', 'Partidul Social Democrat',
 'Volkspartij voor Vrijheid en Democratie', '',
 'Sozialdemokratische Partei Deutschlands', 'EH BILDU',
 'Partito Democratico', 'Partidul Mișcarea Populară',
 'Ciudadanos – Partido de la Ciudadanía', 'Liberal Democrats',
 'Freie Demokratische Partei', 'Movimento 5 Stelle', 'Les Républicains',
 'SMER-Sociálna demokracia', 'Christlich Demokratische Union Deutschlands',
 'Christen Democratisch Appèl', 'Liberal-Conservative Refomists',
 'Arbetarepartiet- Socialdemokraterna', 'Österreichische Volkspartei',
 'La République en marche', 'Partido Nacionalista Vasco',
 'SPOLU – občianska demokracia', 'Europe Écologie', 'Vänsterpartiet',
 'Partidul Naţional Liberal', 'Svoboda a přímá demokracie',
 'Lietuvos socialdemokratų partija',
 'Fidesz-Magyar Polgári Szövetség-Kereszténydemokrata Néppárt', 'Volt',
 'Slovenska ljudska stranka', 'Socijaldemokratska partija Hrvatske',
 'Parti du Travail de Belgique', 'Nieuw-Vlaamse Alliantie',
 'Piratenpartei Deutschland', 'Socialni demokrati',
 "Ecologistes Confédérés pour l'Organisation de Luttes Originales",
 'Prawo i Sprawiedliwość', 'Mouvement Démocrate',
 'Ökologisch-Demokratische Partei', 'The Brexit Party', 'Azione',
 'Liste Renaissance', 'Partido Socialista', 'Partit Nazzjonalista',
 'Partij van de Arbeid', 'Ano 2011', 'Mouvement Réformateur',
 'Venstre, Danmarks Liberale Parti', 'Democratic Rally',
 'Sojusz Lewicy Demokratycznej - Unia Pracy', 'Les centristes',
 'Labour Party', 'PRO Romania', 'Momentum', 'ChristenUnie',
 'Independents for change', 'DIE LINKE.', 'Groen',
 'Democratic Unionist Party', 'Christlich-Soziale Union in Bayern e.V.',
 'Südtiroler Volkspartei', 'VMRO', 'GroenLinks', 'JA21', 'Freie Wähler',
 'Plaid Cymru - Party of Wales', 'Europa Verde',
 'Partido Comunista Português', "Fratelli d'Italia", 'Fine Gael Party',
 'Istarski demokratski sabor - Dieta democratica istriana',
 'Elliniki Lusi-Greek Solution', 'Christen-Democratisch & Vlaams',
 'Socialdemokratiet', 'NEOS – Das Neue Österreich',
 'Progressive Party of Working People - Left - New Forces',
 'Familien-Partei Deutschlands', 'USR-PLUS', 'Place publique',
 'Parti démocratique', 'Partidul Puterii Umaniste', 'PIRÁTI',
 'Lista Marjana Šarca', 'Independente', 'Bloco de Esquerda',
 'JOBBIK MAGYARORSZÁGÉRT MOZGALOM', 'Freiheitliche Partei Österreichs',
 'Perussuomalaiset', 'Conservative Party',
 'Parti chrétien social luxembourgeois', 'Vihreä liitto',
 'Partij voor de Dieren', 'Sozialdemokratische Partei Österreichs',
 'Suomen Sosialidemokraattinen Puolue/Finlands Socialdemokratiska Parti',
 'Polskie Stronnictwo Ludowe', 'Progresívne Slovensko',
 'Miljöpartiet de gröna', 'Bulgarian Socialist Party', 'Attīstībai/Par!',
 'Democraten 66', 'Solidarna Polska Zbigniewa Ziobro',
 'Tėvynės sąjunga-Lietuvos krikščionys demokratai', 'Sloboda a Solidarita',
 'Panhellenic Socialist Movement - Olive Tree',
 'Sotsiaaldemokraatlik Erakond', "Partija 'VIENOTĪBA'",
 'Democrats for Strong Bulgaria', 'Liberalerna', 'Suomen Keskusta',
 'Fianna Fáil Party', 'Agir - La Droite constructive', 'Dansk Folkeparti',
 'Moderaterna', '-', 'Komunistická strana Čech a Moravy', 'Nouvelle Donne',
 'Kristdemokraterna', 'Alliance Party of Northern Ireland',
 'Partit dels Socialistes de Catalunya', 'Sverigedemokraterna',
 'Eesti Konservatiivne Rahvaerakond', 'Gauche républicaine et socialiste',
 'Democratic Party',
 "Nacionālā apvienība 'Visu Latvijai!'-'Tēvzemei un Brīvībai/LNNK'",
 'Det Radikale Venstre',
 'Partido do Centro Democrático Social-Partido Popular',
 'Déi Gréng - Les Verts', 'Vasemmistoliitto', 'Independiente',
 'TOP 09 a Starostové', 'Communist Party of Greece',
 'Nova Slovenija – Krščanski demokrati', 'Delegación Ciudadanos Europeos',
 'Movement for Social Democracy EDEK', 'Kansallinen Kokoomus',
 'Izquierda Unida', 'Starostové a nezávisli',
 'Obyčajní ľudia a nezávislé osobnosti', 'Slovak PATRIOT',
 'Hrvatska demokratska zajednica', 'Esquerra Republicana de Catalunya',
 'Mouvement Radical Social-Libéral', 'PODEMOS',
 'Lietuvos valstiečių ir žaliųjų sąjunga',
 'Staatkundig Gereformeerde Partij',
 'Parti ouvrier socialiste luxembourgeois', 'Indépendent', 'Živi Zid',
 'Křesťanská a demokratická unie - Československá strana lidová',
 'Die PARTEI', 'Kresťanskodemokratické hnutie',
 'Partidul Naţional Ţaranesc Creştin Democrat',
 'Lietuvos lenkų rinkimų akcija – Krikščioniškų šeimų sąjunga',
 'Hrvatska konzervativna stranka', 'Slovenska demokratska stranka',
 'Eesti Keskerakond', 'Svenska folkpartiet', 'Občanská demokratická strana',
 'Hnutie Republika', 'Magyar Szocialista Párt', 'ANTICAPITALISTAS',
 'Catalunya en Comú', "'Saskaņa' sociāldemokrātiskā partija",
 'Darbo partija', 'Die Grünen - Die Grüne Alternative',
 'Socialistische Partij.Anders', 'Open Vlaamse Liberalen en Democraten',
 'Enhedslisten', 'Uniunea Democrată Maghiară din România',
 'Det Konservative Folkeparti', 'Latvijas Krievu savienība', 'Italia Viva',
 'Junts per Catalunya - Lliures per Europa', 'Isamaa',
 'Partij voor de Vrijheid']



indicecountry= np.zeros((811, 28))

for i in range(len(listecountry)):
    for j in range(len(countries)):
       
        if listecountry[i]==countries[j]:
            indicecountry[i][j]=1

print(indicecountry)

indice_party = np.zeros((811, 207))

for i in range(len(liste_party)):
    for j in range(len(party)):     
        if liste_party[i] == party[j]:
            indice_party[i][j] = 1

print(indice_party)

indice_epg = np.zeros((811, 9))

for i in range(len(liste_epg)):
    for j in range(len(epg)):     
        if liste_epg[i] == epg[j]:
            indice_epg[i][j] = 1

print(indice_epg)
"""


###
"""
indice_votes = np.array(liste_result_votes)
indice_votes = indice_votes.T

fmt = "%d"
np.savetxt('votes_12544.csv', indice_votes, delimiter=".", fmt = fmt)
"""
###

"""
np.savetxt('indice_epg.csv', indice_epg, delimiter=".", fmt = fmt)
np.savetxt('indice_party.csv', indice_party, delimiter=".", fmt = fmt)
np.savetxt('indice_country.csv', indicecountry, delimiter=".", fmt = fmt)
"""