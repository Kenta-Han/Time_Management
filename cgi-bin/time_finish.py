#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi,cgitb,MySQLdb,datetime,sys
from datetime import date

# DBに接続しカーソルを取得する
connect = MySQLdb.connect(host='localhost', user='root', passwd='mysql', db='time_management', charset='utf8')
c = connect.cursor()

now = datetime.datetime.today() ## 現在の日付を取得
form = cgi.FieldStorage()
user_name = form.getvalue('user_name')
user_id = form.getvalue('user_id')
password = form.getvalue('password')
datetime_finish = form.getvalue('datetime_finish')

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
"""
print(html_body)

## idを検索
sql_search_id = "select max(id) from main_table where user_id='" + user_id + "';"
c.execute(sql_search_id)
sql_id = c.fetchone()[0]

## finish_timeをupdate
sql_update = "update main_table set finish_time='" + datetime_finish + "' where id='" + str(sql_id) + "';"
c.execute(sql_update)
connect.commit()

print("<h2 class='msg_to_user'>" + str(user_name) + "さん．お疲れ様でした！</h2>")

print("<div class='time_button'>")
print("<button onclick='history.back()' class='button_back'/>戻る</button>")

print("<form action='sign_in.py' method='post' >")
logout = '' ## 空要素
print("<input type='hidden' name='user_id' value='" + logout + "'>")
print("<input type='hidden' name='password' value='" + logout + "'>")
print("<input type='submit' value='ログアウト' class='button_sign_out'/>")
print("</form>")
print("</div>")

print("</body></html>")

c.close
connect.close
