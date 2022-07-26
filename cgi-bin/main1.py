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


with open('template/main1.html','r', encoding='utf-8') as portada:
    file = portada.read()
    print(file.format('Consultas Kpop', """
    
     <div class="jumbotron text-center">
        <h1>Haga su consulta</h1>
    </div>

    <div id="content">
      <form action="consulta1.py" method="get">
          <fieldset>
              <legend> Ingresar consulta 1 </legend>
              <!-- Text input-->
              <div>
                  <label>
                    <textarea name="input" id="input" class="form-control" rows="25" cols="50" maxlength="500" required></textarea><br>
                  </label>
              </div>

              <!-- Button -->
              <div>
                  <input class="submit" type="submit" value="Consultar">
              </div>

          </fieldset>
      </form>
  </div>
  """))