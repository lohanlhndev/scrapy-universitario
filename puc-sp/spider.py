import requests
from bs4 import BeautifulSoup

page_cursos = requests.get('https://portal.fundasp.org.br/matriculagrad/listas/01/01chamada.html')
soup_cursos = BeautifulSoup(page_cursos.content, 'html.parser')
cursos = soup_cursos.find('tbody').find_all('a')

link = [curso.get('href') for curso in cursos]
nome_curso = [curso.text for curso in cursos]


i = 0
while i < len(nome_curso):

    f = open('teste.txt', 'a', newline="", encoding="utf-8")
    f.write('\ncurso: '+nome_curso[i].split(':')[0]+'\n')
    f.close()

    page = requests.get('https://portal.fundasp.org.br/matriculagrad/listas/01/'+link[i])
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find_all('td')
    nomes = [nome.text for nome in table]

    
    n = 4
    while n < len(nomes):
        f = open('teste.txt', 'a', newline="", encoding="utf-8")
        f.write(nomes[n]+'\n')  
        f.close()

        n += 2

    
    i += 1



