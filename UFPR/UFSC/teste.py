import requests
from bs4 import BeautifulSoup

page = requests.get('http://dados.coperve.ufsc.br/vestibular2020/resultado/vestcac03_Curso4601.html')
soup = BeautifulSoup(page.content, 'lxml')
teste = soup.find_all('td', {'align': 'left'})
font = [font.find('font').text for font in teste]

print(font)