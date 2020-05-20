from bs4 import BeautifulSoup
import requests 

url_base = 'http://resultados03.acafe.org.br/vestibular/2020/1/resultado/instituicao.html'
page_base = requests.get(url_base)
bs_base = BeautifulSoup(page_base.content, 'html.parser')

instituiocoes = bs_base.find('body').find('font')
inst = [teste.find('a').get('href') for teste in instituiocoes if teste.find('a') != -1 and teste.find('a') is not None]

for link in inst:
    url_inst = 'http://resultados03.acafe.org.br/vestibular/2020/1/resultado/'+str(link).replace(' ', '%20').replace('\\', '/')
    page_inst = requests.get(url_inst)
    bs_inst = BeautifulSoup(page_inst.content, 'html.parser')
    
    campus = bs_inst.find('body').find('font')
    camp = [teste.find('a').get('href') for teste in campus if teste.find('a') != -1 and teste.find('a') is not None]
    #print(camp)
    for link_c in camp:        
        link_base = link.split('\\')
        
        url_curso = 'http://resultados03.acafe.org.br/vestibular/2020/1/resultado/'+ str(link_base[0]) +'/'+str(link_c)
        page_cuso = requests.get(url_curso)
        bs_curso = BeautifulSoup(page_cuso.content, 'html.parser')

        cursos = bs_curso.find('body').find('font')
        curso = [teste.find('a').get('href') for teste in cursos if teste.find('a') != -1 and teste.find('a') is not None]
        nome_curso = [teste.find('a').text for teste in cursos if teste.find('a') != -1 and teste.find('a') is not None]

        

        for link_a in range(len(curso)):
            f = open('teste.txt', 'a', newline="", encoding="utf-8")
            f.write('\ncurso: '+nome_curso[link_a]+'\n')
            f.close()

            url_aprov = 'http://resultados03.acafe.org.br/vestibular/2020/1/resultado/' + str(link_base[0]).replace(' ', '%20')+'/'+ str(curso[link_a])
            page_aprov = requests.get(url_aprov)
            bs_aprov = BeautifulSoup(page_aprov.content, 'html.parser')
            
            table = bs_aprov.find('table').find_all('tr')


            nomes = [t.find('td').find('div').text for t in table]
            #print(nomes)
            i = 2

            while i < len(nomes):
                f = open('teste.txt', 'a', newline="", encoding="utf-8")
                f.write(nomes[i]+'\n')
                f.close()
                i += 1
                





