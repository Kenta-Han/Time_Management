#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi,cgitb,MySQLdb,datetime,sys
from Crypto.Cipher import AES

# DBに接続しカーソルを取得する
connect = MySQLdb.connect(host='localhost', user='root', passwd='mysql', db='time_management', charset='utf8')
c = connect.cursor()

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

## ログイン
print("<form action='time_schedule_in.py' method='post'>")
print("<div class='d_sign_in'>")
print("<h3>ユーザID：<input type='text' name='user_id' style='width: 250px;height: 26px;font-size:16px;'></h3>")
print("<h3>パスワード：<input type='password' name='password' style='width: 250px;height: 26px;font-size:16px;'></h3>")
print("<input type='submit' value='ログイン' class='button_sign_in'/>")
print("</div>")
print("</form>")

 ## 新規登録
print("<form action='sign_up.py' method='post'>")
print("<div class='d_sign_up'>")
print("<input type='submit' value='新規登録' class='button_sign_up'/>")
print("</div>")
print("</form>")

print("</body></html>")

c.close
connect.close
