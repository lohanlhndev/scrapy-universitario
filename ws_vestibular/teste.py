from bs4 import BeautifulSoup
import requests

url = 'http://resultados04.acafe.org.br/vestibular/2020/1/resultado/FURB/aprovados_8050.html'
page = requests.get(url)
bs = BeautifulSoup(page.content, 'html.parser')

table = bs.find('table').find_all('tr')
teste = [t.find('td').find('div').text for t in table]


print(teste)
