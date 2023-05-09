import numpy as np
import pandas as pd
import re
from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()

df = pd.read_csv("./data/hotel.csv")
del (df['Unnamed: 0'])
del (df['note_utilisateur'])
# print(df['equipement'].unique())
liste_equipement_valorisant = ["Free High Speed Internet (WiFi)",
                               'Bar / lounge', "Fitness Center with Gym / Workout Room",
                               "Parking",
                               "Breakfast", 'Free breakfast', "Restaurant", "Pool"]

df['equipement'] = df["equipement"].apply(lambda x: eval(x))

liste_equipement_unique = []
for i in liste_equipement_valorisant:
    df[i] = 0
# fonctionne jusqu'au row 220 car les prochains sont des listes de listes")
for i in range(220, len(df['equipement'])):
    liste_temp = []
    for j in df["equipement"][i]:
        liste_temp += j
    df["equipement"][i] = list(set(liste_temp))
for i in range(len(df['equipement'])):
    for j in df['equipement'][i]:
        if (type(j) == str):
            if (j in liste_equipement_valorisant):
                df[j][i] = 1

df.dropna(inplace=True)


def nettoyer_note(x):
    if re.match("^[0-9]\.[0-9]", x):
        return x[:3]
    else:
        pass


def convertir_liste_en_moyenne(liste):
    res = []
    for element in liste:
        res.append(float(element))
    if len(res) != 0:
        return (sum(res) / len(res))
    else:
        return 0


df['note'].iloc[:220] = df['note'].iloc[:220].apply(lambda x: nettoyer_note(x))
df['note'].iloc[220:] = df['note'].iloc[220:].apply(lambda x: eval(x))

for i in range(220, len(df['note'])):
    liste_temp = []
    if df['note'][i] != None:
        for j in df["note"][i]:
            if j != "":
                liste_temp.append(j)
        df["note"][i] = list(set(liste_temp))

for i in range(220, len(df['note'])):
    liste_temp = []
    if df['note'][i] != None:
        for j in df['note'][i]:
            liste_temp.append(j[:3])
        df['note'][i] = convertir_liste_en_moyenne(liste_temp)

list_pays = ['Rome', 'Amsterdam', 'Paris', 'Dublin', 'Berlin', 'Madrid', 'Munich', 'London', 'Barcelona']
df['adresse'].iloc[220:] = df['adresse'].iloc[220:].apply(lambda x: eval(x))
df['Ville'] = 0
for i in range(220, len(df['adresse'])):
    for j in df['adresse'][i]:
        for k in list_pays:
            if k in j:
                df['Ville'][i] = k

for i in df['adresse'].head():
    if type(i) == float:
        i = np.nan

for i in range(1, len(df['adresse'].head(221))):
    try:
        for j in df.loc['adresse', i]:
            for k in list_pays:
                if k in j:
                    df['Ville'][i] = k
                else:
                    df['Ville'][i] = "NA"
    except KeyError as err:
        df['Ville'][i] = np.nan

df['prix'] = df['prix'].apply(lambda x: eval(x))
df['prix_moyenne'] = 0
for i in range(len(df['prix'])):
    try:
        for j in df['prix'][i]:
            if type(j) == list:
                for k in j:
                    liste_prix = re.findall(r'€\d+', k)
                    liste_prix_int = []
                    for prix in liste_prix:
                        prix_int = int(prix[1:])
                        liste_prix_int.append(prix_int)
                    if len(liste_prix_int) != 0:
                        df['prix_moyenne'][i] = liste_prix_int[0]
    except KeyError as err:
        df['prix_moyenne'][i] = np.nan

del (df['equipement'])

del (df['prix'])
for i in range(len(df['adresse'].head(220))):
    for j in list_pays:
        try:
            if (j in df['adresse'][i]):
                df['Ville'][i] = j
        except KeyError as err:
            df['Ville'][i] = np.nan

df['titre'].iloc[220:] = df['titre'].iloc[220:].apply(lambda x: eval(x))
for i in range(263, len(df['titre'])):
    df['titre'][i] = df['titre'][i][0]



df.to_csv("test.csv")
