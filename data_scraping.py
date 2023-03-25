from functools import partial

import pandas as pd
from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import multiprocessing

filename = "liste_hotel_europe.txt"  # nom du fichier à lire
lines = []  # liste pour stocker les lignes du fichier
l_prix = []
l_titre = []
l_adresse = []
l_equipement = []
l_note_utilisateur = []
l_note = []

# ouverture du fichier en mode lecture
with open(filename, "r") as file:
    # boucle sur chaque ligne du fichier
    for line in file:
        # suppression des caractères de fin de ligne (\n ou \r\n)
        line = line.strip()
        # ajout de la ligne à la liste
        lines.append(line)


def divide_list(lst):
    sublist_size = len(lst) // 10
    sublists = []
    for i in range(10):
        start = i * sublist_size
        end = start + sublist_size
        sublists.append(lst[start:end])
    return sublists


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


def recuperer_all_features(url, l_note_utilisateur=l_note_utilisateur, l_titre=l_titre, l_adresse=l_adresse,
                           l_equipement=l_equipement, l_prix=l_prix):
    options = webdriver.ChromeOptions()
    options.add_argument("--disk-cache-dir=Z:/Cache_chrome")
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    id_titre = "HEADING"
    class_adresse = "fHvkI PTrfg".split(" ")
    classe_prix = "lqzkg"
    css_note_utilisateur = ".uwJeR"
    css_equipement = "div.ssr-init-26f:nth-child(1)"
    classe_note = "JXZuC"

    try:
        note_utilisateur = driver.find_element(By.CSS_SELECTOR, css_note_utilisateur).text
    except NoSuchElementException:
        l_note_utilisateur.append("")
    except StaleElementReferenceException:
        l_note_utilisateur.append("")
    else:
        l_note_utilisateur.append(note_utilisateur)

    try:
        titre = driver.find_element(By.ID, id_titre).text
    except NoSuchElementException:
        l_note_utilisateur.append("")
    except StaleElementReferenceException:
        l_note_utilisateur.append("")
    else:
        l_titre.append(titre)

    try:
        prix = driver.find_elements(By.CLASS_NAME, classe_prix)
    except NoSuchElementException:
        l_prix.append("")
    except StaleElementReferenceException:
        l_prix.append("")
    else:
        temp = []
        for i in prix:
            temp.append(i.text)
        l_prix.append(temp)

    try:
        equipement = driver.find_element(By.CSS_SELECTOR, css_equipement).text.split("\n")
    except NoSuchElementException:
        l_equipement.append("")
    except StaleElementReferenceException:
        l_equipement.append("")
    else:
        l_equipement.append(equipement)

    try:
        adresse = driver.find_element(By.CLASS_NAME, "fHvkI").text

    except NoSuchElementException:
        l_adresse.append("")
    except StaleElementReferenceException:
        l_adresse.append("")

    else:
        l_adresse.append(adresse)

    try:
        note = driver.find_element(By.CLASS_NAME, classe_note).get_attribute("aria-label")
    except NoSuchElementException:
        l_note.append("")
        print(url)
    except StaleElementReferenceException:
        l_note.append("")
        print(url)
    else:
        l_note.append(note)

    listes = (l_titre, l_prix, l_equipement, l_adresse, l_note, l_note_utilisateur)

    driver.quit()
    return listes


l_prix = []
l_titre = []
l_adresse = []
l_equipement = []
l_note_utilisateur = []
l_note = []

"""for i in urls:
    driver = webdriver.Chrome(options=options)
    recuperer_all_features(i, l_note_utilisateur, l_titre, l_adresse, l_equipement, l_prix)"""

if __name__ == "__main__":
    sous_listes_URL = divide_list(lines)
    urls = sous_listes_URL[5]

    pool = multiprocessing.Pool(processes=10)
    scraping = pool.map(recuperer_all_features, urls)

    l_titre = []
    l_prix = []
    l_equipement = []
    l_adresse = []
    l_note = []
    l_note_utilisateur = []

    for liste in scraping:
        l_titre.append(liste[0])
        l_prix.append(liste[1])
        l_equipement.append(liste[2])
        l_adresse.append(liste[3])
        l_note.append(liste[4])
        l_note_utilisateur.append(liste[5])

    dico = {}
    dico["titre"] = l_titre
    dico["note_utilisateur"] = l_note_utilisateur
    dico["equipement"] = l_equipement
    dico["prix"] = l_prix
    dico["adresse"] = l_adresse
    dico["note"] = l_note
    df = pd.DataFrame(dico)
    df.to_csv("test_200_hotel_5.csv")
