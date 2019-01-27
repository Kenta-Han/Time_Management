#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi,cgitb,MySQLdb,datetime,sys,json
import mypackage.aescipher as myp_aesc

# DBに接続しカーソルを取得する
conn = MySQLdb.connect(host='localhost', user='root', passwd='mysql', db='time_management', charset='utf8')
cur = conn.cursor()
print('Content-type: text/html\nAccess-Control-Allow-Origin: *\n')

cgitb.enable()
form = cgi.FieldStorage()
user_name = form.getvalue('user_name')
birthday = form.getvalue('birthday')
user_id = form.getvalue('user_id')
password = form.getvalue('password')
password_re = form.getvalue('password_re')
mail = form.getvalue('mail')

cipher = myp_aesc.AESCipher("PkDv17c6xxiqXPrvG2cUiq90VIrERfthHuViKapv6E1F7E0IgP")
password = cipher.encrypt(password).decode("utf8") ## 暗号化
password_re = cipher.encrypt(password_re).decode("utf8") ## 暗号化

sql_insert = "INSERT INTO user(name, birthday, user_id, password, password_re, mail) VALUES(%s,%s,%s,%s,%s,%s);"
cur.execute(sql_insert,(user_name,birthday,user_id,str(password),str(password_re),mail))
conn.commit()

res_json = {"message":"Yes"}
print(json.dumps(res_json))
