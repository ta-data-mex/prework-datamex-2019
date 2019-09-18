# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 12:55:32 2019

@author: luisf
"""


"""
01.Apocalypsis

Cargas un arsenal de armas y una mochila con cargadores de munición de tamaño variable para algunos tipos de armas. ¿Cuántos zombies puedes matar antes de tener que echar a correr por tu vida? Deberás imprimir el resultado de cada caso que corresponde al número de balas que tienes de las armas que cargas.
ALGORITMO: Por cada arma diferente que cargas, tienes que comprobar si portas cargadores para ella. Si esto es afirmativo deberás sumar el total de balas que podrás disparar.
"""

###############################################################################
###########      #Caso 0: Ejemplo simple
###############################################################################

armas = ['pistola','escopeta']

cargadores = {
    'pistola': [10, 10], 
    'escopeta': [2, 2, 2, 2, 2]
}

for x in armas:
    for y, z in cargadores.items():
        if x == y:
            print("Total de municiones para",y,":",sum(z))

###############################################################################
#########   Caso 1: Mismas armas que municiones
###############################################################################

armas = ['pistola', 'ametralladora', 'escopeta', 'fusil de francotirador']

cargadores = {
    'pistola': [12, 13, 4, 5, 20, 17], 
    'ametralladora': [33, 40], 
    'escopeta': [2, 2, 2, 1], 
    'fusil de francotirador': [1, 2, 4]
}

for x in armas:
    for y, z in cargadores.items():
        if x == y:
            print("Total de municiones para",y,":",sum(z))

###############################################################################
#########   Caso 2: Más tipos de munición que armas
###############################################################################

armas = ['pistola', 'ametralladora', 'escopeta', 'fusil de francotirador']

cargadores = {
    'pistola': [12, 13, 4, 5, 20, 17], 
    'ametralladora': [33, 40], 
    'escopeta': [2, 2, 2, 1], 
    'fusil de francotirador': [1, 2, 4], 
    'bazoka': [1, 1]
}

for x in armas:
    for y, z in cargadores.items():
        if x == y:
            print("Total de municiones para",y,":",sum(z))

###############################################################################
#########   Caso 3: Más armas que tipos de munición
###############################################################################

armas = ['pistola', 'ametralladora', 'escopeta', 'fusil de francotirador']

cargadores = {
    'pistola': [12, 13, 4, 5, 20, 17], 
    'ametralladora': [33, 40], 
    'escopeta': [2, 2, 2, 1] 
}

for x in armas:
    for y, z in cargadores.items():
        if x == y:
            print("Total de municiones para",y,":",sum(z))

#Notas:
#1.- para acceder a las llaves dentro de un diccionario es .keys() ya los valores .values(), y a todo .items()