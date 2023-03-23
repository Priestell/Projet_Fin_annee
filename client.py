import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


options = Options()
options.set_preference("javascript.enabled", False)
driver = webdriver.Firefox(options=options)
url = "https://www.tripadvisor.com/Hotels-g187147-Paris_Ile_de_France-Hotels.html"
driver.get(url)


classe_name = "property_title"
liste = driver.find_elements(By.CLASS_NAME, "property_title")
URLS_des_hotels = []
urls_des_pages = []
for i in range(1,34):
    urls_des_pages.append("https://www.tripadvisor.com/Hotels-g187147-oa" + str(i * 30) + "-Paris_Ile_de_France-Hotels.html")

for i in urls_des_pages:
    driver.get(i)
    liste = driver.find_elements(By.CLASS_NAME, "property_title")
    for j in liste:
        URLS_des_hotels.append(j.get_attribute("href"))

with open("liste.txt", "w") as fichier:
    for element in URLS_des_hotels:
        fichier.write(element + "\n")