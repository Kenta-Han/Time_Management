#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi,cgitb,MySQLdb,datetime,sys
from datetime import date

# DBに接続しカーソルを取得する
connect = MySQLdb.connect(host='localhost', user='root', passwd='mysql', db='time_management', charset='utf8')
c = connect.cursor()

now = datetime.datetime.today() ## 現在の日付を取得
form = cgi.FieldStorage()
user_id = form.getvalue('user_id')
password = form.getvalue('password')
datetime_start = form.getvalue('datetime_start')

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

ymd = datetime_start.split()[0]

year = ymd.split("-")[0] ## 年
month = ymd.split("-")[1] ## 月
day = ymd.split("-")[2] ## 日
weekday = date(int(year),int(month),int(day)).isoweekday() ## 曜日

sql_insert = "insert into main_table(user_id,password,year,month,day,weekday,start_time) values(%s,%s,%s,%s,%s,%s,%s);"

c.execute(sql_insert,(user_id,password,year,month,day,weekday,datetime_start))
connect.commit()

c.execute("select name from user where user_id='" + str(user_id) + "' and password='" + str(password) + "';")
name = c.fetchone()[0]

print("<h2 class='msg_to_user'>" + str(name) + "さん．今日も頑張りましょう！</h2>")

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
