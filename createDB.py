import mimetypes
import os
import sqlite3
import Helper.settings

from django.http import HttpResponse
from xlsxwriter import Workbook

# Функция создания базы данных, запускать только один раз при ее создании
def First_Init():
    adr = "/var/www/u0825496/data/www/ruthelp.ru/Helper/Helper/db_access/db_s.db"
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
                        gender TEXT NULL,
                        confirm boolean );""")

    StringSQLtext = "INSERT INTO comments ( surname, name, lname, group2, number, typeconcession, gender, confirm ) VALUES ( '"+ 'Фамилия' +"', '"+ 'Имя' +"', '"+'Отчетство'+"', '"+'Группа'+"', '"+'Моб. телефон'+"', '"+'Причина'+"', '"+'Пол'+"', '"+'Есть оригинал'+"' ); "
    cursor.execute(StringSQLtext)
    conn.commit()
    conn.close()
    print('Successfully create DB!')
    return

First_Init()
