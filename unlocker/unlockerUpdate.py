#!/usr/bin/python

import sqlite3
import os

def UnlockerUpdate(imei, timestamp, code):
    dbfile = os.path.dirname(__file__) + "\\unlocker.db"
    conn = sqlite3.connect(dbfile)
    c = conn.cursor()
    print("Opened database successfully")
    c.execute("UPDATE UNLOCKER SET CODE='%s' WHERE IMEI='%s' AND TIMESTAMP='%s'"%(code,imei,timestamp))
    conn.commit()
    print("Total number of rows updated :" + str(conn.total_changes))
    conn.close()
    return 'IMEI与时戳对应验证码已经更新！'