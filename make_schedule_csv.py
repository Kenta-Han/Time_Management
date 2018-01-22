import sys, os, datetime, openpyxl

YOUBI = ['月','火','水','木','金','土','日']

input_date = input('作成する年月度を入力してください（例：201608）：')
try:
    # 当月の初日
    month_first = datetime.datetime.strptime(input_date, '%Y%m')
except ValueError:
    input('年月を201801のように入力してください。')
    sys.exit()

# 前月の末日
month_last = month_first - datetime.timedelta(days = 1)

# 勤怠管理の開始日と終了日（20日締め）
date_start = month_last.replace(day = 21)
date_end = month_first.replace(day = 20)

# エクセルブックファイル（ひな形）
file_template = '勤怠管理表.xlsx'
book = openpyxl.load_workbook(file_template)

# エクセルシート
sheet = book.get_sheet_by_name('Sheet1')

# 年月度の入力
sheet.cell(row = 1, column = 1).value = month_first.year
sheet.cell(row = 1, column = 3).value = month_first.month

# 月日曜日の入力
for rowNum in range(13, 44):
    if date_start <= date_end:
        # 月
        sheet.cell(row = rowNum, column = 1).value = date_start.month
        # 日
        sheet.cell(row = rowNum, column = 2).value = date_start.day
        # 曜日
        sheet.cell(row = rowNum, column = 3).value = YOUBI[date_start.weekday()]
    date_start += datetime.timedelta(days = 1)

# 新規ブックファイル保存
file_new = month_first.strftime('%Y%m') + '_' + file_template
book.save(file_new)
