# Býr til account fyrir kennara á mysql serverinum
# og username = username úr csv skjalinu password = pass.123
# og þeir hafa aðgang að búa til database undir
# notandanafnÞeirra_nafnÁdatabase
import csv,pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='pass.123')
cur = conn.cursor()

with open("lokaverk_v18.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=',')
    data = list(reader)
for x in data:
    username = x[3]
    password = "pass.123"
    create = "CREATE USER '"+username+"'@'%' IDENTIFIED BY '"+password+"';"
    cur.execute(create)
    grant = "grant all on `"+username+"\_%`.* to `"+username+"`@`%`;"
    cur.execute(grant)

conn.commit()
cur.close()
conn.close()
