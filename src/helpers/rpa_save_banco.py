import requests
from bs4 import BeautifulSoup
from .save_app import save_daddos_banco

def Rpa_lista_Nomes():

    url = 'https://exame.com/pop/os-100-nomes-de-bebes-masculinos-mais-populares-em-2022/'

    response = requests.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Encontrando todos os elementos 'li' dentro da tag 'ol'
        nomes = soup.find('ol').find_all('li', class_='sc-1761b25b-0 eZnvxA body-extra-large')
        
        cpfs="12312321"
        endereco="rua paranagi 53"
        telefones="(81)988380290"
        for nome in nomes:
            #save_daddos_banco(nome.text,cpfs,endereco,telefones) comentei para nao ficar salvando direto no banco de dados
            print(nome.text)
    else:
        print('Erro ao fazer a requisição HTTP:', response.status_code)