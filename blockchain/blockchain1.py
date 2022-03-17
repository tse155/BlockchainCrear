# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 10:32:19 2022

@author: the_c
"""

#Crear una cadena de bloques
#Para instalar:
#Flask==0.12.2: pip install Flask==1.1.2
#Cliente HTTP Postman: https://www.getpostman.com/

#Importar librerías

#cada bloque de la cadena debe tener su propio timestamp
import datetime
#hashlib:libreria para generar los hashes de las cadenas de bloques
import hashlib
#se importa Json: JavaScript object notation
import json
#vamos a importar el constructor Flask, que permite crear un objeto flask
from flask import Flask, jsonify 

#Parte 1: crear una cadena de bloques
#orientada a objetos

class Blockchain:
    
    def __init__(self):
        self.chain=[]
        self.create_block(proof=1, previous_hash= "0")

#Parte 2: minar un bloque de la cadena