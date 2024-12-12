import pandas as pd
import requests
import json
import openpyxl
import re

# 判斷是否維中文字串
def IsChinese(contents):
  zhPattern =re.compile(u'[\u4e00-\u9fa5]+')
  if zhPattern.search(contents):
    return True
  else:
    return False

# 打算要取得的股票代碼
stock_list_tse = ['2330', '2454', '3034', '2379', '2498']
stock_etf_list_tse = ['0050', '0056', '0061', '00713', '00915', '00919']
bond_etf_list_otc = ['00725B', '00751B', '00761B', '00772B']

# 組合API需要的股票清單字串
stock_list1 = '|'.join('tse_{}.tw'.format(stock) for stock in stock_list_tse)
stock_etf_list1 = '|'.join('tse_{}.tw'.format(stock_etf) for stock_etf in stock_etf_list_tse)
bond_etf_list1 = '|'.join('otc_{}.tw'.format(bond_etf) for bond_etf in bond_etf_list_otc)

#　組合完整的URL
stock_list = stock_list1 + '|' + stock_etf_list1 + '|' + bond_etf_list1
 # print(stock_list)
query_url = f'http://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch={stock_list}'

# 呼叫股票資訊API
response = requests.get(query_url)

# 判斷該API呼叫是否成功
if response.status_code != 200:
  raise Exception('取得股票資訊失敗.')
# else:
#  print(response.text)

# 將回傳的JSON格式資料轉成Python的dictionary
data = json.loads(response.text)
#print(data)

# 過濾出有用到的欄位
columns = ['c','n','z','tv','v','o','h','l','y', '%', 'd']
df = pd.DataFrame(data['msgArray'], columns=columns)
df.columns = ['股票代號','公司簡稱','成交價','成交量','累積成交量','開盤價','最高價','最低價','昨收價','資料更新時間', '日期']

# 清除(缺失值)多餘行並顯示股票資訊
# df.to_excel('Stocks Price 1.xlsx' , index=False )
# df = df.dropna(axis=0)
# print(df['成交價'].describe())

# 自行新增漲跌百分比欄位
df.insert(9, "漲跌百分比", 0.0)

# 用來計算漲跌百分比的函式
for index, row in df.iterrows():
  if df.at[index, '成交價'] == "-":
    df.at[index, '漲跌百分比'] = "-"
  else:
    df.at[index, '漲跌百分比'] = (float(df.at[index, '成交價']) - float(df.at[index, '昨收價'])) / float(df.at[index, '昨收價']) * 100

"""def count_per(x):
  if isinstance(x[0], float) == False:
    x[0] = 0.0

  result = (x[0] - float(x[1])) / float(x[1]) * 100

  return pd.Series(['-' if x[0] == 0.0 else x[0], x[1], '-' if result == -100 else result])

# 填入每支股票的漲跌百分比
#df[['成交價', '昨收價', '漲跌百分比']] = df[['成交價', '昨收價', '漲跌百分比']].apply(count_per, axis=1)

# 紀錄更新時間
def time2str(t):
  # print(t)
  t = int(t) / 1000 + 8 * 60 * 60. # UTC時間加8小時為台灣時間

  return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t))

# 把API回傳的秒數時間轉成容易閱讀的格式
df['資料更新時間'] = df['資料更新時間'].apply(time2str)
"""
# 將結果存成Excel file
df.to_excel('Stocks Price.xlsx',sheet_name='Stocks Price', index=False)

# 自動調整Excel欄寬
wb = openpyxl.load_workbook('Stocks Price.xlsx')
ws = wb['Stocks Price']


for col in ws.columns:
  maxLen = 0
  column = col[0].column_letter
  for cell in col:
    if IsChinese(str(cell.value)):
      curLen = len(str(cell.value)) * 5
      #print('find chinese', cell, curLen, maxLen)
    else:
      curLen = len(str(cell.value))

    if curLen > maxLen:
      maxLen = curLen

    set_col_width = maxLen + 2

  ws.column_dimensions[column].width = set_col_width


wb.save('Stocks Price.xlsx')
wb.close()
# 顯示股票資訊
print(df)

