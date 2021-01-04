# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 20:41:28 2020

@author: Brandon
Obtener palabra mas frecuenre de los articulos
"""
import nltk
import re
from nltk.corpus import stopwords
from bs4 import BeautifulSoup

#quito la parte del html, solo me quedo con el texto
stopwords = set(stopwords.words('spanish'))
f=open('e961024.htm',encoding='utf-8')
text=f.read()
f.close()
#print(text[:50])
text=nltk.word_tokenize(text)
print("----------------------------------------")
#print(text[:50])

y=0
z=0
articulos={}
w=""
paso=0
for palabra in text:
    if palabra=="title":
        if y==1:
            paso=1
        y=1
        w+=palabra+" "
    if y==1:
        w+=palabra+" "
    if paso==1:
        articulos[z]=w
        w=" "
        paso=0
        z+=1

#articulo=3
#print(articulos[articulo])
print("-----------------------------------")
def quitarCaracter(cadena,letra):
	return cadena.replace(letra," ")
i=0
for w in articulos:
    #print(i)                          
    articulos[i]=quitarCaracter(articulos[i],"<")
    articulos[i]=quitarCaracter(articulos[i],"ban_editorial.gif")
    articulos[i]=quitarCaracter(articulos[i],">")
    articulos[i]=quitarCaracter(articulos[i],"href")
    articulos[i]=quitarCaracter(articulos[i],".html")
    articulos[i]=quitarCaracter(articulos[i],"/a")
    articulos[i]=quitarCaracter(articulos[i],"//")
    articulos[i]=quitarCaracter(articulos[i],"http")
    articulos[i]=quitarCaracter(articulos[i],"/font")
    articulos[i]=quitarCaracter(articulos[i],"font")
    articulos[i]=quitarCaracter(articulos[i],"/title")
    articulos[i]=quitarCaracter(articulos[i],"gifs")
    articulos[i]=quitarCaracter(articulos[i],"align")
    articulos[i]=quitarCaracter(articulos[i],"right")
    articulos[i]=quitarCaracter(articulos[i],"h5")
    articulos[i]=quitarCaracter(articulos[i]," b ")
    articulos[i]=quitarCaracter(articulos[i],"title")
    articulos[i]=quitarCaracter(articulos[i],"size")
    articulos[i]=quitarCaracter(articulos[i],"=")
    articulos[i]=quitarCaracter(articulos[i],"img")
    articulos[i]=quitarCaracter(articulos[i],"src")
    articulos[i]=quitarCaracter(articulos[i],":")
    articulos[i]=quitarCaracter(articulos[i],"hr")
    articulos[i]=quitarCaracter(articulos[i]," p ")
    articulos[i]=quitarCaracter(articulos[i],"/p")
    articulos[i]=quitarCaracter(articulos[i],"basefont")
    articulos[i]=quitarCaracter(articulos[i],"/")
    articulos[i]=quitarCaracter(articulos[i],'""')
    articulos[i]=quitarCaracter(articulos[i],"''")
    articulos[i]=quitarCaracter(articulos[i],'-')
    articulos[i]=quitarCaracter(articulos[i],' rt ')
    articulos[i]=quitarCaracter(articulos[i],'center')
    articulos[i]=quitarCaracter(articulos[i],' h ')
    articulos[i]=quitarCaracter(articulos[i],'www.excelsior.com.mx')
    for w in range(0,10):
        articulos[i]=quitarCaracter(articulos[i],str(w))
    i+=1
longitud=i
#print(articulos[articulo])

print("Numero de articulos: ",i)
topicos=("crisis","privatización","contaminación","política","economía","tecnología","televisa")
print(articulos[1])

#minuscula
for i in range(0,longitud):
    articulos[i]=articulos[i].lower()

#print(articulos[2])
from array import *
import csv
import numpy as np

final={}
n = len(topicos)
m = longitud
a = [[0] * m for i in range(n)]
#print(len(a[0]))

for i in range(1,longitud):
    y=0
    for topic in topicos:
        a[y][i]=((articulos[i].count(topic))/7)*100
        y+=1
print("----------------------------------------------")
print(a)

'''
#guardar en una tabla
with open('tabla.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(a)
'''