from bs4 import BeautifulSoup
import requests

i = 1
while i < 200:
    url = 'http://portal.nc.ufpr.br/documentos/PS2020/resultado1fase/'+str(i).zfill(3)+'.html'
    page = requests.get(url)
    bs = BeautifulSoup(page.content, 'html.parser')

    print(url)
    if page.ok == True:
        curso = bs.find('div', {'class': 'panel-body'}).find('h4').find('strong').text
        table = bs.find('table', {'id': 'dataTable-Publicacao'}).find('tbody').find_all('tr')
        nome = [teste.find_all('td')[1].text  for teste in table]

        f = open('teste.txt', 'a', newline="", encoding="utf-8")
        f.write('\ncurso: '+curso.split('-')[0]+'\n')
        f.close()
        n = 0
        while n < len(nome):
            f = open('teste.txt', 'a', newline="", encoding="utf-8")
            f.write(nome[n]+'\n')
            f.close()
            n+= 1
    i += 1