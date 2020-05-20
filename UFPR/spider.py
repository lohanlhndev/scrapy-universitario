from bs4 import BeautifulSoup
import requests

page_cursos = requests.get('http://portal.nc.ufpr.br/documentos/PS2020/resultado2fase/resultado_ps2020.html')
soup_cursos = BeautifulSoup(page_cursos.content, 'html.parser')
cursos = soup_cursos.find_all('a')
tds_curso = soup_cursos.find_all('font')
link_curso = [link.get('href') for link in cursos] #2
nome_curso = [curso.text for curso in tds_curso if curso.text != 'Clique aqui'] #4


c = 4
i = 2
while i < len(link_curso):
    f = open('lista.txt', 'a', newline="", encoding="utf-8")
    f.write('\ncurso: '+nome_curso[c].split('-')[0]+'\n')
    f.close()
    page = requests.get('http://portal.nc.ufpr.br/documentos/PS2020/resultado2fase/'+link_curso[i])
    soup = BeautifulSoup(page.content, 'lxml')
    table = soup.find_all('table')[3]
    tr= table.find_all('tr')
    teste = [td.find_all('td')[1] for td in tr]
    n = 1
    while n < len(teste):
        f = open('lista.txt', 'a', newline="", encoding="utf-8")
        f.write(teste[n].text+'\n')
        f.close()
        n+=1
    c+=1
    i+=1