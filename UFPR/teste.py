import requests
from bs4 import BeautifulSoup

page = requests.get('http://portal.nc.ufpr.br/documentos/PS2020/resultado2fase/001.html')
soup = BeautifulSoup(page.content, 'lxml')
teste = soup.find_all('td', {'align': 'left'})

print(teste)