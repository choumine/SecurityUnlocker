#!/usr/bin/python

import sqlite3
import os

def UnlockerInsert(imei, timestamp):
    dbfile = os.path.dirname(__file__) + "\\unlocker.db"
    conn = sqlite3.connect(dbfile)
    c = conn.cursor()
    print("Opened database successfully")
    c.execute("INSERT INTO UNLOCKER (IMEI,TIMESTAMP) \
               VALUES ('%s', '%s')"%(imei,timestamp))
    conn.commit()
    print("Records created successfully")
    conn.close()
    return 'IMEI与时戳已经记录！'