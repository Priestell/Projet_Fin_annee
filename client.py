from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

filename = "liste_.txt" # nom du fichier à lire
lines = [] # liste pour stocker les lignes du fichier


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

