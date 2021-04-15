from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd

base_url = 'https://it.wikipedia.org/wiki/Calciatore_dell%27anno_(PFA)'

page = requests.get(base_url)

if page.status_code == requests.codes.ok:
    bs = BeautifulSoup(page.text, 'lxml')
    #print(  BeautifulSoup(page.text))


players = bs.find('table', class_='wikitable').findAll('tr')[1:2]

country = players.findAll('a')


print(players)
print(country)
