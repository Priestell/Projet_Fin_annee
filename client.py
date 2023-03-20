from selenium import webdriver
import requests
import bs4
from selenium.webdriver.common.by import By

clss = "/html/body/div[2]/div[1]/div/div[6]/div/div/div/div[1]/div[1]/h1"
url = "https://www.tripadvisor.com/Hotel_Review-g187147-d228694-Reviews-Hotel_Malte_Astotel-Paris_Ile_de_France.html"
driver = webdriver.Firefox()
driver.get(url)
titre = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[6]/div/div/div/div[1]/div[1]/h1") # Chemin vers
print(titre.text)

amenities_div = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[4]/div/div[1]/div[4]/div/div/div/div/div[2]/div[2]/div[1]/div[2]")
suite = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[4]/div/div[1]/div[4]/div/div/div/div/div[2]/div[2]/div[1]/div[5]")
#note = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[4]/div/div[1]/div[4]/div/div/div/div/div[2]/div[2]/div[3]/div[1]/div[2]/span/svg")
print(amenities_div.text)
print(suite.text)
#print(note.text)
# récupérez les textes des équipements de l'établissement

driver.quit()
