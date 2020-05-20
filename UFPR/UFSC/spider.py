from bs4 import BeautifulSoup
import requests

page_cursos = requests.get('http://dados.coperve.ufsc.br/vestibular2020/resultado/vestcac03_LinkCursos.html')
soup_cursos = BeautifulSoup(page_cursos.content, 'html.parser')
cursos = soup_cursos.find_all('a')

link_cursos = [link.get('href') for link in cursos]
nome_curso = [curso.text for curso in cursos]

i = 0
while i < len(link_cursos):

    f = open('lista.txt', 'a', newline="", encoding="utf-8")
    f.write('\ncurso: '+nome_curso[i].split('-')[0]+'\n')
    f.close()

    page = requests.get('http://dados.coperve.ufsc.br/vestibular2020/resultado/'+link_cursos[i])
    soup = BeautifulSoup(page.content, 'html.parser')
    teste = soup.find_all('td', {'align': 'left'})
    nome = [font.find('font').text for font in teste]
    
    n = 0
    while n < len(nome):
        f = open('lista.txt', 'a', newline="", encoding="utf-8")
        f.write(nome[n]+'\n')
        f.close()
        n+=1

    i+=1


