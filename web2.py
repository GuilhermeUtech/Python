from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()

driver.get("https://statusinvest.com.br/acoes/abev3")

content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")

nome = soup.find(class_="lh-4")
preco = soup.find(class_="value")

print("Nome: "+nome.text+"\nPreço: "+preco.text)


