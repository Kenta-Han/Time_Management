#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi,cgitb,MySQLdb,datetime,sys,json
import mypackage.aescipher as myp_aesc

# DBに接続しカーソルを取得する
conn= MySQLdb.connect(host='localhost', user='root', passwd='mysql', db='time_management', charset='utf8')
cur = conn.cursor()
print('Content-type: text/html\nAccess-Control-Allow-Origin: *\n')

cgitb.enable()
form = cgi.FieldStorage()
user_id = form.getvalue('user_id')
password = form.getvalue('password')

cur.execute("SELECT * FROM user WHERE user_id='" + str(user_id) + "';")
user_info_kari = []
for i in cur:
    user_info_kari.append(i)

## ユーザIDがない場合
if not user_info_kari:
    res_json = {"message":""}
    res_json["message"] = "ユーザが見つかりませんでした"
    print(json.dumps(res_json))
## ユーザIDがある場合
else:
    cipher = myp_aesc.AESCipher("PkDv17c6xxiqXPrvG2cUiq90VIrERfthHuViKapv6E1F7E0IgP")
    db_password = cipher.decrypt(user_info_kari[0][4].encode("utf8")) ## 複号化

    ## パスワードが合致するの場合
    if db_password.decode("utf8") == password:
        cur.execute("SELECT * FROM user WHERE user_id='" + str(user_id) + "' AND password='" + str(user_info_kari[0][4]) + "';")
        user_info = []
        for i in cur:
            user_info.append(i)

        res_json = {"message":"Yes"}
        print(json.dumps(res_json))
    else:
        res_json = {"message":"パスワードが異なります．"}
        print(json.dumps(res_json))
