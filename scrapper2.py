# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

class beca():
    _link = ""
    _titulo = ""

    def __init__(self,link,titulo):
        self._link = link
        self._titulo = titulo

    def show(self):
        print (self._titulo + " " + self._link)

# Realizamos la petición a la web
request = requests.get("https://becas.agora-santander.com/?lang=es")
becas = []
# Comprobamos que la petición nos devuelve un Status Code = 200
status_code = request.status_code
if status_code == 200:
    # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
    html = BeautifulSoup(request.text, "html.parser")
    # Buscamos los class item
    entradas = html.find_all('li', {'class': 'item'})
    # Recorremos todas las entradas para extraer el título, link.
    for i, entrada in enumerate(entradas):

        if entrada.find('div', {'class': 'ins c open'}) is not None:
            link = entrada.find('div', {'class': 'link'}).get('data-href')
            titulo = entrada.find('p', {'class': 'ellipsis'}).getText()
            index = beca(link,titulo)
            becas.append(index)
else:
    print "Status Code %d" % status_code

# Mas scraping aquí La Caixa etc...



# !Mas scraping aquí La Caixa etc...

# Mostramos todas las becas scrapeadas
for x in range(0,len(becas)):
    becas[x].show()



