#!/usr/bin/python3
#-*- coding: utf-8 -*-
from configparser import ConfigParser
import psycopg2
import mysql.connector
import hashlib
import sys

class DB:
    def __init__(self, host, user, password, database):
        self.db = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.db.cursor() 


    def get_data_consulta(self, consulta):
        sql = f''' {consulta}
           '''

        self.cursor.execute(sql)
        return self.cursor.fetchall()