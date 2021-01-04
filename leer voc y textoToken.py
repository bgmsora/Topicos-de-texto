# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 01:39:26 2020

@author: Brandon
"""
import nltk
#obtener vocabulario
f=open('vocabulario.txt')
vocabulary=f.read()
f.close()
i=0
vocabulary=nltk.word_tokenize(vocabulary)
voc=[]

for palabra in vocabulary:
    if i%2==0:
        w=palabra
    else:
        w=w+' '+palabra
        if palabra=="n":
            voc.append(w)
        del(w)
    i+=1
print(voc[:1])

f=open('textoTokenLematizado.txt')
texto=f.read()
f.close()
i=0
texto=nltk.word_tokenize(texto)
text=[]
#n de sustantivo
for palabra in texto:
    if i%2==0:
        w=palabra
    else:
        w=w+' '+palabra
        if palabra=="n":
            text.append(w)
        del(w)
    i+=1
print(text[:1])

result={}
for abc in voc:
    i=0
    for palabra in text:
        if abc==palabra:
            i+=1
    result[abc]=i

import operator
result=sorted(result.items(),
               key=operator.itemgetter(1),
               reverse=True)

#print(result)

f=open('masComunPalabras.txt','w')
for palabra in result:
    #print(palabra)
    f.write(str(palabra)+"\n")
f.close()