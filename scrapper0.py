# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 11:47:26 2017

@author: Santi
"""

from bs4 import BeautifulSoup
import requests

# Realizamos la petición a la web
request = requests.get("https://obrasociallacaixa.org/es/educacion-becas/otras-becas/en-un-vistazo", verify=False)

# Comprobamos que la petición nos devuelve un Status Code = 200
status_code = request.status_code
if status_code == 200:
    # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
    html = BeautifulSoup(request.text, "html.parser")
    # Buscamos los class item
    entradas = html.find_all('div', {'class': "journal-content-article"})
    # Recorremos todas las entradas para extraer el título, link.
    for i, entrada in enumerate(entradas):
        if((entrada.find('div', {'class':"contenido_becas"}) is not None) and (entrada.find('span', {'class': "cuadrado_blanco"}) is not None)):
            if (entrada.find('span', {'class': "cuadrado_blanco"}).find("Cerrada") is None):
                link = entrada.find('a').get('href')
                titulo = entrada.find('h3').getText()
                numBecas = entrada.find('p').getText()
                estado = entrada.find('span', {'class':"cuadrado_blanco"}).getText().strip()
                print ("Beca: " , link, "\n Titulo: " ,titulo ,"\n Numero: ", numBecas, "\n Estado: ", estado)
else:
    print ("Status Code %d" % status_code)