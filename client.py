import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

l_nom = []
l_note = []
l_amenities = []
l_equipment = []


def recuperer(l_nom, l_note, l_amenities, l_equipment):
    dico = {}
    titre = driver.find_element(By.XPATH,
                                "/html/body/div[2]/div[1]/div/div[6]/div/div/div/div[1]/div[1]/h1")  # Chemin vers le
    # titre
    l_nom.append(titre.text)
    amenities_div = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[4]/div/div[1]/div["
                                                  "4]/div/div/div/div/div[2]/div[2]/div[1]/div[2]")
    suite = driver.find_element(By.XPATH,
                                "/html/body/div[2]/div[2]/div[2]/div[4]/div/div[1]/div[4]/div/div/div/div/div[2]/div["
                                "2]/div[1]/div[5]")
    # prix = driver.find_element(By.CLASS_NAME, "WXMFC b")
    note = driver.find_element(By.CSS_SELECTOR, ".uwJeR")
    l_note.append(note.text)
    liste_ = amenities_div.text.split("\n")
    l_amenities.append(liste_)
    liste_des_equipement = suite.text.split("\n")
    l_equipment.append(liste_des_equipement)


urls = [
    "https://www.tripadvisor.com/Hotel_Review-g187147-d230431-Reviews-Hotel_Astoria_Astotel-Paris_Ile_de_France.html",
    "https://www.tripadvisor.com/Hotel_Review-g187147-d228694-Reviews-Hotel_Malte_Astotel-Paris_Ile_de_France.html",
    "https://www.tripadvisor.com/Hotel_Review-g187147-d197424-Reviews-Novotel_Paris_Les_Halles-Paris_Ile_de_France.html",
    "https://www.tripadvisor.com/Hotel_Review-g187147-d197946-Reviews-Hotel_Bradford_Elysees_Astotel"
    "-Paris_Ile_de_France.html",
    "https://www.tripadvisor.com/Hotel_Review-g187147-d10159593-Reviews-Hotel_La_Comtesse-Paris_Ile_de_France.html",
    "https://www.tripadvisor.com/Hotel_Review-g187147-d9566832-Reviews-Hotel_34B_Astotel-Paris_Ile_de_France.html",
    "https://www.tripadvisor.com/Hotel_Review-g187147-d228848-Reviews-Hotel_Lorette_Astotel-Paris_Ile_de_France.html",
    "https://www.tripadvisor.com/Hotel_Review-g780713-d289828-Reviews-Hotel_L_Elysee_Val_D_Europe"
    "-Serris_Marne_la_Vallee_Seine_et_Marne_Ile_de_France.html",
    "https://www.tripadvisor.com/Hotel_Review-g187147-d232552-Reviews-La_Maison_Favart-Paris_Ile_de_France.html",
    "https://www.tripadvisor.com/Hotel_Review-g187147-d228779-Reviews-Hotel_Marignan_Champs_Elysees"
    "-Paris_Ile_de_France.html"
]
driver = webdriver.Firefox()

for i in urls:
    driver.get(i)
    recuperer(l_nom, l_note, l_amenities, l_equipment)
dico = {}
dico["titre"] = l_nom
dico["note_utilisateur"] = l_note
dico["commodité"] = l_amenities
dico["equipement"] = l_equipment
df = pd.DataFrame.from_dict(dico)
print(df)
df.to_csv("dix_meilleur_hotel_scrapper.csv")