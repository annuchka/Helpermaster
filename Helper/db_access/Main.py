import mimetypes
import os
import sqlite3
import Helper.settings

from django.http import HttpResponse
from xlsxwriter import Workbook

GenderMass = ["женский", "мужской"]
adr = Helper.settings.BASE_DIR + "/Helper/db_access/db_s.db"
# ТОЛЬКО ДЛЯ REG.RU
#adr.replace('\\','/')



# Функция добавления данных в БД, если такой записи нету
def Insert_Data(gender, group, surname, name, lastname, number, typeconcession, chooseDoc):
    gender = GenderMass[int(gender)]
    conn = sqlite3.connect(adr)
    cursor = conn.cursor()
    StringSQLtext = "SELECT * FROM comments WHERE surname = '"+surname+"' AND name = '"+name+"' AND lname = '"+lastname+"' AND group2 = '"+group+"' AND number = '"+number+"' AND typeconcession = '"+typeconcession+"' AND gender = '"+gender+"'"
    cursor.execute(StringSQLtext)
    mysel = cursor.fetchall()
    if mysel != []:
        return
    # добавление записи
    StringSQLtext = "INSERT INTO comments ( surname, name, lname, group2, number, typeconcession, gender ) VALUES ( '"+surname+"', '"+name+"', '"+lastname+"', '"+group+"', '"+number+"', '"+typeconcession+"', '"+gender+"' ); "
    cursor.execute(StringSQLtext)
    conn.commit()
    conn.close()
    return

# Функция генерации экселя по данным из БД
def Get_Data():
    conn = sqlite3.connect(adr)
    c = conn.cursor()
    workbook = Workbook('db_accel.xlsx')
    worksheet = workbook.add_worksheet()
    #c.execute("select * from comments")

    c.execute("select surname, name, lname, group2, number, typeconcession, gender, Confirm from comments")
    mysel = c.execute("select surname, name, lname, group2, number, typeconcession, gender, Confirm from comments")
    for i, row in enumerate(mysel):
        for j, value in enumerate(row):
            worksheet.write(i, j, row[j])
    workbook.close()
    conn.close()
    File_Path = os.path.abspath('db_accel.xlsx')
    fp = open(File_Path, "rb")
    response = HttpResponse(fp.read())
    fp.close()
    file_type = mimetypes.guess_type(File_Path)
    if file_type is None:
        file_type = 'application/octet-stream'
    response['Content-Type'] = file_type
    response['Content-Length'] = str(os.stat(File_Path).st_size)
    response['Content-Disposition'] = "attachment; filename=Spisok_Podavshix.xlsx"

    # Чистка временнойго файла
    os.remove(File_Path)
    return response
