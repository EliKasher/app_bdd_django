#!/usr/bin/python3
#-*- coding: utf-8 -*-
from asyncio.windows_events import NULL
import cgi
import os
import sys
import filetype
import re
from db import DB
import html
import itertools

print("Content-type: text/html; charset=UTF-8")
print()
sys.stdout.reconfigure(encoding='utf-8')

db = DB('localhost', 'root', '', 'kpop')

form = cgi.FieldStorage()

if(form.getvalue('input') != None):
  consulta = html.escape(form['input'].value)
else:
  print("No hubo una consulta válida")

consulta = (consulta)

data_consulta1 = db.get_data_consulta(consulta)

tabla = """
            <div class="container ">
            <table class="table">
        <thead>
        <tr>
        <th scope="col">Nombre Canción</th>
        <th scope="col">Nombre Artista 1</th>
        <th scope="col">Nombre Artista 2</th>
        </tr>
        </thead>
        <tbody>
        """
        
if (data_consulta1!= None):
    for p in data_consulta1:
      tabla+=f""" 
          <tr>
        <td>{p[0]}</td>
        <td>{p[1]}</td>
        <td>{p[2]}</td>
        </tr>
        """

tabla+="""
    </tbody>
    </table>
    </div> """


with open('template/consulta1.html','r', encoding='utf-8') as portada:
    file = portada.read()
    print(file.format('Consultas Kpop', tabla))
