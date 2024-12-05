""" Module providing functions to access SQLite3 databass """
import sqlite3
import datetime
import time

conn = sqlite3.connect('money20.db2')
print("Opened database successfully")

cursor = conn.execute("SELECT objid, type, displayname, currencytype, balance,"
                      " hide, sindex, rate, top, snote, lsupdate  from Account")


for row in cursor:
    print("Object ID = ", row[0])
    print("Type = ", row[1])
    print("Display Name = ", row[2])
    print("Currency Type = ", row[3])
    print("Balance = ", row[4])
    print("Hide = ", row[5])
    print("SIndex = ", row[6])
    print("Rate = ", row[7])
    print("Top = ", row[8])
    print("Note = ", row[9])
    date_offset = (datetime.datetime(1970, 1, 1) -
                   datetime.datetime(1899, 12, 30)).total_seconds() + (8*60*60)
    last_update_time = (row[10]*24*60*60) - date_offset
    # t1 = time.ctime(lastupdate_time)
    t1 = time.localtime(last_update_time)
    t2 = time.strftime('%Y/%m/%d %H:%M:%S', t1)
    print("Update time = ", t2, "\n")

conn.close()
print("Closed database successfully")
