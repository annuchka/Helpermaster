import mimetypes
import os
import sqlite3

from django.http import HttpResponse
from xlsxwriter import Workbook

# Функция создания базы данных, запускать только один раз при ее создании
def First_Init():
    adr = "/Helper/Helper/db_access/db_s.db"
    conn = sqlite3.connect(adr)
    cursor = conn.cursor()
    # Создание таблицы
    cursor.execute("""  CREATE TABLE comments (
                        post_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        surname TEXT NOT NULL,
                        name TEXT NOT NULL,
                        lname TEXT NOT NULL,
                        group2 TEXT NOT NULL,
                        number TEXT NULL,
                        typeconcession TEXT NOT NULL,
                        gender TEXT NULL);""")
    conn.commit()
    conn.close()
    return

First_Init()
