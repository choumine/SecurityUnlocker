#!/usr/bin/python

import sqlite3
import os

def UnlockerSelect():
    dbfile = os.path.dirname(__file__) + "\\unlocker.db"
    conn = sqlite3.connect(dbfile)
    c = conn.cursor()
    print("Opened database successfully")
    cursor = c.execute("SELECT * FROM UNLOCKER")
    s = ""
    for row in cursor:
        s += "----------<br />"
        s += "ID = %s%s"%(str(row[0]),"<br />")
        s += "IMEI = %s%s"%(row[1],"<br />")
        s += "TIMESTAMP = %s%s"%(row[2],"<br />")
        s += "CODE = %s%s"%(row[3],"<br />")
        s += "----------<br />"
    print("Operation done successfully")
    conn.close()
    return s