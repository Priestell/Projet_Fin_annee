import pandas as pd
import re
import re

import pandas as pd

df = pd.read_csv("./data/hotel.csv")
del (df['Unnamed: 0'])
del (df['note_utilisateur'])
liste_equipement_valorisant = ["Free High Speed Internet (WiFi)",
                               'Bar / lounge', "Fitness Center with Gym / Workout Room",
                               "Parking",
                               "Breakfast", 'Free breakfast', "Restaurant", "Pool"]
df['equipement'] = df["equipement"].apply(lambda x: eval(x))
liste_equipement_unique = []

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


list_pays = ['Rome', 'Amsterdam', 'Paris', 'Dublin', 'Berlin', 'Madrid', 'Munich', 'London', 'Barcelona']
df['adresse'].iloc[220:] = df['adresse'].iloc[220:].apply(lambda x: eval(x))
df['Ville'] = ""

for i in df['adresse'].head():
    if type(i) == float:
        i = "NA"

for i in range(1,len(df['adresse'])):
    try:
        print(df['adresse'][i])
    except KeyError as err:
        print('aucune donnée')

"""for i in df['adresse'].head(4):
    print(i)"""