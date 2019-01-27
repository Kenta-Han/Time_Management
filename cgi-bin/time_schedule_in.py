#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi,cgitb,MySQLdb,datetime,sys,json
import mypackage.aescipher as myp_aesc

# DBに接続しカーソルを取得する
conn= MySQLdb.connect(host='localhost', user='root', passwd='mysql', db='time_management', charset='utf8')
cur = conn.cursor()
print('Content-type: text/html\nAccess-Control-Allow-Origin: *\n')

form = cgi.FieldStorage()
user_id = form.getvalue('user_id')
password = form.getvalue('password')

# html_body = u"""
# <!DOCTYPE html>
# <head>
# <meta http-equiv="content-type" content="text/html; charset=utf-8" />
# <script src="https://code.jquery.com/jquery-3.0.0.min.js"></script>
# <link href='/data/stylesheet.css' rel='stylesheet' type='text/css' />
# <title>勤怠管理</title>
# </head>
#
# <body>
# <header><h1>勤怠管理</h1></header>
# <h2 style= 'text-align:center;'>登録完了しました．</h2>
# """
# print(html_body)

# res = []
# res_json = {"message":""}
# res_json["message"] = 12
# # print("<h1>")
# # print(res_json)
# # print("</h1>")
# # res.append(res_json)
# # print(json.dumps(res))
# print(json.dumps(res_json)) # 送信

cur.execute("SELECT * FROM user WHERE user_id='" + str(user_id) + "';")
user_info_kari = []
for i in cur:
    user_info_kari.append(i)

## ユーザIDがない場合
if not user_info_kari:
    # print("<h1 style='text-align:center;'> ユーザが見つかりませんでした． </h1>")
    # print("<div class='d_nouser'>")
    # print("<form action='sign_in.py' method='post'>")
    # print("<input type='submit' value='ログイン' class='button_sign_in'/>")
    # print("</form>")
    # print("<form action='sign_up.py' method='post'>")
    # print("<input type='submit' value='新規登録' class='button_sign_up'/>")
    # print("</form>")
    # print("</div>")
    res_json = {"message":""}
    res_json["message"] = "ユーザが見つかりませんでした"
    print(json.dumps(res_json))
#
# ## ユーザIDがある場合
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
#
#         print("<table class='timetable'>")
#         print("<thead><tr><th colspan=8>ユーザ情報</td></tr></thead>")
#         print("<tbody><tr><th colspan=5>ユーザ名</th><td>" + str(user_info[0][1]) + "</td></tr>")
#         print("<tr><th colspan=5>生年月日</th><td>" + str(user_info[0][2]) + "</td></tr>")
#         print("<tr><th colspan=5>ユーザID</th><td>" + str(user_info[0][3]) + "</td></tr>")
#         # print("<tr><th colspan=5>パスワード</th><td>" + str(user_info[0][4]) + "</td></tr>")
#         print("<tr><th colspan=5>メールアドレス</th><td>" + str(user_info[0][6]) + "</td></tr>")
#         print("</tbody></table>")
#
#         now = datetime.datetime.today() ## 現在の日付を取得
#         ##print(now) ## 2010-05-08 15:42:00.731000
#
#         print("<div class='time_button'>")
#         print("<form action='time_start.py' method='post' style='display:inline;'>")
#         print("<input type='hidden' name='user_name' value='" + str(user_info[0][1]) + "'>")
#         print("<input type='hidden' name='user_id' value='" + str(user_id) + "'>")
#         print("<input type='hidden' name='password' value='" + str(password) + "'>")
#         print("<input type='hidden' name='datetime_start' value='" + str(now) + "'>")
#         print("<input type='submit' value='出勤' class='button_start'/>")
#         print("</form>")
#
#         print("<form action='time_finish.py' method='post' style='display:inline;'>")
#         print("<input type='hidden' name='user_name' value='" + str(user_info[0][1]) + "'>")
#         print("<input type='hidden' name='user_id' value='" + str(user_id) + "'>")
#         print("<input type='hidden' name='password' value='" + str(password) + "'>")
#         print("<input type='hidden' name='datetime_finish' value='" + str(now) + "'>")
#         print("<input type='submit' value='帰宅' class='button_finish'/>")
#         print("</form>")
#
#         print("<form action='sign_in.py' method='post' >")
#         logout = '' ## 空要素
#         print("<input type='hidden' name='user_id' value='" + logout + "'>")
#         print("<input type='hidden' name='password' value='" + logout + "'>")
#         print("<input type='submit' value='ログアウト' class='button_sign_out'/>")
#         print("</form>")
#         print("</div>")
#
#     ## パスワードが合致しないの場合
#     else :
#         print("<h1 style='text-align:center;'> パスワードが間違っています． </h1>")
#         print("<div class='d_nouser'>")
#         print("<form action='sign_in.py' method='post'>")
#         print("<input type='submit' value='ログイン' class='button_sign_in'/>")
#         print("</form>")
#         print("<form action='sign_up.py' method='post'>")
#         print("<input type='submit' value='新規登録' class='button_sign_up'/>")
#         print("</form>")
#         print("</div>")
#
# print("</body></html>")

# c.close
# connect.close()
