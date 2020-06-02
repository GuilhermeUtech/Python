from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()

driver.get("https://www.google.com/search?q=petr4&oq=petr&aqs=chrome.0.69i59j69i57j69i59j0l2j69i60l3.663j1j7&sourceid=chrome&ie=UTF-8")

content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")

nome = soup.find(class_="oPhL2e")
print("Nome da empresa: "+ nome.text)