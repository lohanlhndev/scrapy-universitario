from bs4 import BeautifulSoup
import requests

page_cursos = requests.get('https://cps.uepg.br/inicio/pss_2019/1/Resultado_UEPG_PSS.htm')
soup_cursos = BeautifulSoup(page_cursos.content, 'html.parser')
cursos_nome = soup_cursos.find_all('td')
nome_curso = [curso.text for curso in cursos_nome]
cursos_link = soup_cursos.find_all('a')
link = [curso.get('href') for curso in cursos_link]

curso = 8 
# while curso < len(nome_curso):
#     f = open('teste2.txt', 'a', newline="", encoding="utf-8")
#     f.write('\ncurso: '+nome_curso[curso].split(':')[0]+'\n')
#     f.close()
#     curso += 5

i = 0
while i < len(link):
    f = open('teste2.txt', 'a', newline="", encoding="utf-8")
    f.write('\ncurso: '+nome_curso[curso].split(':')[0]+'\n')
    f.close()

    page_nomes = requests.get('https://cps.uepg.br/inicio/pss_2019/1/'+link[i])
    soup_nomes = BeautifulSoup(page_nomes.content, 'html.parser')
    td_nomes = soup_nomes.find_all('td')

    nome = [nome.find('font').text for nome in td_nomes]

    n = 16
    while n <len(nome):
        
        f = open('teste2.txt', 'a', newline="", encoding="utf-8")
        f.write(nome[n]+'\n')
        f.close()
        n += 11
    curso +=5
    i += 2
