import pandas as pd
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

filename = "liste_hotel_europe.txt"  # nom du fichier à lire
lines = []  # liste pour stocker les lignes du fichier
l_prix = []
l_titre = []
l_adresse = []
l_equipement = []
l_note  = []

# ouverture du fichier en mode lecture
with open(filename, "r") as file:
    # boucle sur chaque ligne du fichier
    for line in file:
        # suppression des caractères de fin de ligne (\n ou \r\n)
        line = line.strip()
        # ajout de la ligne à la liste
        lines.append(line)


def recuperer_url(url):
    options = Options()
    options.set_preference("javascript.enabled", False)
    driver = webdriver.Firefox(options=options)
    url = "https://www.tripadvisor.com/Hotels-g187147-Paris_Ile_de_France-Hotels.html"
    driver.get(url)

    classe_name = "property_title"
    liste = driver.find_elements(By.CLASS_NAME, "property_title")
    URLS_des_hotels = []
    urls_des_pages = []
    for i in range(1, 34):
        urls_des_pages.append(
            "https://www.tripadvisor.com/Hotels-g187147-oa" + str(i * 30) + "-Paris_Ile_de_France-Hotels.html")

    for i in urls_des_pages:
        driver.get(i)
        liste = driver.find_elements(By.CLASS_NAME, "property_title")
        for j in liste:
            URLS_des_hotels.append(j.get_attribute("href"))

    with open("liste_hotel_paris.txt", "w") as fichier:
        for element in URLS_des_hotels:
            fichier.write(element + "\n")


def recuperer_url_(url, urls_des_pages):
    options = Options()
    options.set_preference("javascript.enabled", False)
    driver = webdriver.Firefox(options=options)
    URLS_des_hotels = []
    for i in urls_des_pages:
        driver.get(i)
        liste = driver.find_elements(By.CLASS_NAME, "property_title")
        for j in liste:
            URLS_des_hotels.append(j.get_attribute("href"))

    with open("liste_hotel_europe.txt", "w") as fichier:
        for element in URLS_des_hotels:
            fichier.write(element + "\n")


def recuperer_all_features(url, l_note, l_titre, l_adresse, l_equipement, l_prix):
    driver.get(url)
    id_titre = "HEADING"
    class_adresse = "fHvkI PTrfg".split(" ")
    classe_prix = "lqzkg"
    css_note = ".uwJeR"
    css_equipement = "div.ssr-init-26f:nth-child(1)"

    try:
        note = driver.find_element(By.CSS_SELECTOR, css_note).text
    except NoSuchElementException:
        # Si l'élément n'est pas trouvé, append "l_0" à la liste
        l_note.append(0)
    else:
        # Si l'élément est trouvé, append la valeur i à la liste
        l_note.append(note)

    try:
        titre = driver.find_element(By.ID, id_titre).text
    except NoSuchElementException:
        # Si l'élément n'est pas trouvé, append "l_0" à la liste
        l_note.append(0)
    else:
        # Si l'élément est trouvé, append la valeur i à la liste
        l_titre.append(titre)

    try:
        prix = driver.find_element(By.CLASS_NAME, classe_prix).text.split("\n")[0]
    except NoSuchElementException:
        l_prix.append(0)
    else:
        l_prix.append(prix)

    try:
        equipement = driver.find_element(By.CSS_SELECTOR, css_equipement).text.split("\n")
    except NoSuchElementException:
        l_equipement.append(0)
    else:
        l_equipement.append(equipement)

    try:
        for i in class_adresse:
            l_adresse.append(driver.find_element(By.CLASS_NAME, i).text)
    except NoSuchElementException:
        # Si l'élément n'est pas trouvé, append "l_0" à la liste
        l_note.append(0)
    else:
        for i in class_adresse:
            l_adresse.append(driver.find_element(By.CLASS_NAME, i).text)

URLS = []
driver = webdriver.Firefox()
for i in range(10):
    URLS.append(lines[i])

for i in URLS:
    recuperer_all_features(i, l_note, l_titre, l_adresse, l_equipement, l_prix)

dico = {}

dico["titre"] = l_titre

dico["note"] = l_note

dico["equipement"] = l_equipement

dico["prix"] = l_prix

dico["adresse"] = l_adresse

print(len(dico["titre"]))
print(len(dico["note"]))
print(len(dico["equipement"]))
print(len(dico["prix"]))
print(len(dico["adresse"""]))