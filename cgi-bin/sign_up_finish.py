#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi,cgitb,MySQLdb,datetime,sys
import mypackage.aescipher as myp_aesc

# DBに接続しカーソルを取得する
connect = MySQLdb.connect(host='localhost', user='root', passwd='mysql', db='time_management', charset='utf8')
c = connect.cursor()

now = datetime.datetime.today() ## 現在の日付を取得
form = cgi.FieldStorage()
user_name = form.getvalue('user_name')
birthday = form.getvalue('birthday')
user_id = form.getvalue('user_id')
password = form.getvalue('password')
mail = form.getvalue('mail')

html_body = u"""
<!DOCTYPE html>
<head>
<meta http-equiv="content-type" content="text/html; charset=utf-8" />
<script src="https://code.jquery.com/jquery-3.0.0.min.js"></script>
<link href='/data/stylesheet.css' rel='stylesheet' type='text/css' />
<title>勤怠管理</title>
</head>

<body>
<header><h1>勤怠管理</h1></header>
<h2 style= 'text-align:center;'>登録完了しました．</h2>
"""
print(html_body)

cipher = myp_aesc.AESCipher("PkDv17c6xxiqXPrvG2cUiq90VIrERfthHuViKapv6E1F7E0IgP")
password = cipher.encrypt(password).decode("utf8") ## 暗号化

sql_insert = "insert into user(name, birthday, user_id, password, mail) values(%s,%s,%s,%s,%s);"
c.execute(sql_insert,(user_name,birthday,user_id,str(password),mail))
connect.commit()

## ログイン
print("<form action='time_schedule_in.py' method='post'>")
print("<div class='d_sign_in'>")
print("<h3>ユーザID：<input type='text' name='user_id' style='width: 250px;height: 26px;font-size:16px;'></h3>")
print("<h3>パスワード：<input type='password' name='password' style='width: 250px;height: 26px;font-size:16px;'></h3>")
print("<input type='submit' value='ログイン' class='button_sign_in'/>")
print("</div>")
print("</form>")

print("</body></html>")

c.close
connect.close
