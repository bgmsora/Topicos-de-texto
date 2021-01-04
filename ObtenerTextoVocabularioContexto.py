# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 23:50:19 2020

@author: Brandon
"""
import nltk
from nltk.corpus import stopwords
#obtener vocabulario
f=open('textoLematizado2.txt')
texto=f.read()
f.close()

i=0
texto=nltk.word_tokenize(texto)
text=[]
for palabra in texto:
    if i%2==0:
        w=palabra
    else:
        w=w+' '+palabra
        text.append(w)
        del(w)
    i+=1
#print(text[:100])
#ya estan acomodadas las palabras asi
'''
'e961024 v', 'mod v', 'htm v', 'http v', 'www v', 'excelsior v', 'com v', 'mx v', 
'9610 v', '961024 v', 'art01 v', 'html v', 'excelsior v', 'editorial v',
'''
stopwords = set(stopwords.words('spanish'))
StopWords=[]
for w in stopwords:
    StopWords.append(w+' ')

#print(StopWords)
text2=[]
for w in text:
    no=0
    for stop in StopWords:
        long=len(stop)
        longi=len(w)
        if long<longi:
            if stop[0:long] == w[0:long]:
                no=1
    if no==0:
        text2.append(w)
#print(text2)
##aqui ya le quitamos los stopwords
text2.remove('v v')
text2.remove('vi v')
text2.remove('xii v')
text2.remove('xli v')
text2.remove('xvii v')
text2.remove('xx v')
text2.remove('xxi v')
text2.remove('xxiii v')

f=open('textoTokenizado.txt','w')
for item in text2:
    f.write(item+'\n')
f.close()

#ahora vamos a la lematizacion cambiarlas por sus palabras cercanas
f=open('generateProcesado.txt')
generate=f.read()
f.close()
#print(generate)

#f=open('prueba.txt','w')
generate=nltk.word_tokenize(generate)
i=0
diccionario={}
for palabra in generate:
    if i==0:
        w=palabra
        #print(w)
        i+=1
    elif i==1:
        w=w+' '+palabra[0].lower()
        z=' '+palabra[0].lower()
        i+=1
    else:
        i=0
        #f.write(w+' es igual a'+palabra[0]+'\n')
        diccionario[w]=palabra+z
        #print(w,' es ',diccionario[w])
palabraBuscar='grande v'
#f.close()
#datos corregidos que se copiaron mal o no estaban en el archivo generate
diccionario['según s']='según s'
diccionario['vate v']='vate v'
diccionario['rápidamente r']='rápidamente r'
diccionario['recién r']='recién r'
diccionario['recien r']='recién r'
diccionario['relativamente r']='relativamente r'
diccionario['ver v']='ver v'
diccionario['respectivamente r']='respectivamente r'
diccionario['salvo s']='salvo s'
diccionario['valer v']='valer v'
diccionario['recientemente r']='recientemente r'
diccionario['valorar v']='valorar v'
diccionario['vender v']='vender v'
diccionario['vector v']='vector v'
diccionario['realmente r']='realmente r'
diccionario['viajar v']='viajar v'
diccionario['valle v']='valle v'
diccionario['vencer v']='vencer v'
diccionario['ve v']='ve v'
#diccionario['']=''
diccionario['verbalmente v']='verbalmente v'
diccionario['valor v']='valorar v'
diccionario['vale v']='valorar v'
diccionario['venir v']='venir v'
diccionario['vaticano v']='vaticano v'
diccionario['v v']='v v'
diccionario['vicente v']='vicente v'
diccionario['ir v']='ir v'
'''

'''
#text2.remove('')
text3=[]
for w in text2:
    try:
        text3.append(diccionario[w])
    except:
        if w=='grande v':
            text3.append('grande a')
        else:
            text3.append(w)


##aqui ya le quitamos los stopwords
f=open('textoTokenLematizado.txt','w')
for item in text3:
    f.write(item+'\n')
f.close()

textoRaro=text3;
text3=set(text3)
tokens=sorted(text3)

f=open('vocabulario.txt','w')
for palabra in tokens:
    f.write(palabra+'\n')
f.close()

print(len(tokens))

windowSize=8
contexto=[]
contextoChido={}
for w in tokens:
    contexto=[]
    for i in range(len(textoRaro)):
        if textoRaro[i]==w:
            for j in range(i-int(windowSize/2),i):
                if j >=0:
                    contexto.append(textoRaro[j])
            try:
                for j in range(i+1, i+(int(windowSize/2)+1)):
                    contexto.append(textoRaro[j])
            except IndexError:
                pass
    contextoChido[w]=contexto
    del(contexto)

#print(contextoChido['grande a'])
#guarda los contextos[palabra]
from pickle import dump
output=open('contexto.pkl','wb')
dump(contextoChido,output,-1)
output.close()
