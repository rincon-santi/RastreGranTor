# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 11:47:26 2017

@author: Santi
"""

from bs4 import BeautifulSoup
import requests
import time

# Realizamos la petición a la web
request = requests.get("http://becas.universia.net/busqueda-avanzada", verify=False)

# Comprobamos que la petición nos devuelve un Status Code = 200
status_code = request.status_code
if status_code == 200:
	# Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
	html = BeautifulSoup(request.text, "html.parser")
	# Buscamos los class item
	entradas = html.find_all('div', {'class': "journal-content-article"})
	# Recorremos todas las entradas para extraer el título, link.
	for i, entrada in enumerate(entradas):
		if((entrada.find('a', {'class':"searchBlock-content-title"}) is not None) and (entrada.find('span', {'class': "searchBlock-content-moreinfo-label"}) is not None)):
			link=entrada.find('a', {'class':"searchBlock-content-title"}).getText()
			additionalInfo=""
			es=entrada.find_all('span', {'class':"searchBlock-content-moreinfo-label"})
			for i2, e in enumerate(es):
				additionalInfo=additionalInfo++'\n'++e.getText
			print ("Beca: " , link, additionalInfo)
else:
	print ("Status Code %d" % status_code)