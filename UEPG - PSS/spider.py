from bs4 import BeautifulSoup
import requests

page_cursos = requests.get('https://cps.uepg.br/inicio/verao_2019/1/Resultado_UEPG.htm')
soup_cursos = BeautifulSoup(page_cursos.content, 'html.parser')
cursos = soup_cursos.find_all('a')

link = [curso.get('href') for curso in cursos]
nome_curso = [curso.text for curso in cursos]
#print(nome_curso)

i = 0
while i < len(link):
    
    f = open('teste.txt', 'a', newline="", encoding="utf-8")
    f.write('\ncurso: '+nome_curso[i].split(':')[0]+'\n')
    f.close()

    page_cotas = requests.get('https://cps.uepg.br/inicio/verao_2019/1/'+link[i])
    soup_cotas = BeautifulSoup(page_cotas.content, 'html.parser')
    cotas = soup_cotas.find_all('a')
    link_cotas = [cota.get('href') for cota in cotas]
    #print(link_cotas)
    n = 0
    while n < len(link_cotas):
        if link_cotas[n] is not None:
            page_nomes = requests.get('https://cps.uepg.br/inicio/verao_2019/1/'+link_cotas[n])
            soup_nomes = BeautifulSoup(page_nomes.content, 'html.parser')
            td_nomes = soup_nomes.find_all('td')

            nome = [nome.find('font').text for nome in td_nomes]
            l = 13
            while l < len(nome):
                f = open('teste.txt', 'a', newline="", encoding="utf-8")
                f.write(nome[l]+'\n')
                f.close()
                l +=8                
        n += 2
    i += 1