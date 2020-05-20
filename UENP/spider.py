from bs4 import BeautifulSoup
import requests 

page_cursos = requests.get('https://vestibular.uenp.edu.br/2020/docs/b1875ae5-4fe0-4395-88d1-dde3667054d1/')
soup_cursos = BeautifulSoup(page_cursos.content, 'html.parser')
cursos = soup_cursos.find('tbody').find_all('a')

link = [curso.get('href') for curso in cursos]
nome_curso = [curso.text for curso in cursos]

i = 0
while i < len(nome_curso):

    f = open('teste.txt', 'a', newline="", encoding="utf-8")
    f.write('\ncurso: '+nome_curso[i].split(':')[0]+'\n')
    f.close()

    page_cotas = requests.get('https://vestibular.uenp.edu.br/2020/docs/b1875ae5-4fe0-4395-88d1-dde3667054d1/'+link[i])
    soup_cotas = BeautifulSoup(page_cotas.content, 'html.parser')
    lista_cotas = soup_cotas.find('tbody').find_all('a')
    link_cotas = [cota.get('href') for cota in lista_cotas]
    print(i)
    n = 0
    while n < len(link_cotas):
        print(n)
        page_nomes = requests.get('https://vestibular.uenp.edu.br/2020/docs/b1875ae5-4fe0-4395-88d1-dde3667054d1/'+link_cotas[n])
        soup_nomes = BeautifulSoup(page_nomes.content, 'html.parser')
        if soup_nomes.find('tbody') is not None:
            lista_nomes = soup_nomes.find('tbody').find_all('tr')
            nome = [nome.find_all('td')[2].text for nome in lista_nomes]
            

            l = 0
            while l < len(nome):
                f = open('teste.txt', 'a', newline="", encoding="utf-8")
                f.write(nome[l]+'\n')
                f.close()

                l += 1
        n +=2
    i += 1
