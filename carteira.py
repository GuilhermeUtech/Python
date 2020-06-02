from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import itertools

"""
Consolidador de carteira, objetivo é automatizar o meu trabalho no drive.
['ticket', num_ações]
#tickets[iter].append((tickets[iter][2]) * (tickets[iter][1])) problema ao converter 8,86 pra float
"""
tickets = [['ITSA4', 30], ['KLBN3', 42], ['ENBR3', 10], ['GRND3', 21], ['PETR4', 7], ['MYPK3', 10], ['VINO11', 3], ['MXRF11', 13]]
content = []
nome = []
preco = []
iter = 0

driver = webdriver.Chrome()

for i in tickets:
    driver.get("https://statusinvest.com.br/acoes/"+i[0])
    content.append(driver.page_source)

for i in content:
    soup = BeautifulSoup(i, features="html.parser")
    nome.append(soup.find(class_="lh-4"))
    preco.append(soup.find(class_="value"))

carteira_preco = []

for (i,j) in zip(nome, preco):
    aux = [i.text, j.text]
    aux2 = j.text.replace(",", ".")
    tickets[iter].append(aux2)
    tickets[iter].append(int(tickets[iter][1]) * float(tickets[iter][2]))
    iter+=1

print(tickets)






