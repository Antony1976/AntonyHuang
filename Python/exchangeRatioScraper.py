"""Module providingFunction get exchange ratio."""

import pandas

# 爬取網站
res = pandas.read_html("https://rate.bot.com.tw/xrt?Lang=zh-TW")
# 獲得表格
df = res[0]
# 全部的row(行)以及0~5的index(列)
currency = df.iloc[:, :5]
# 自訂欄位名稱
currency.columns = [u"幣別", u"現金匯率-本行買入",
                    u"現金匯率-本行賣出", u"即期匯率-本行買入", u"即期匯率-本行賣出"]
# 修正’幣別’欄位
currency[u"幣別"] = currency[u"幣別"].str.extract("\((\w+)\)")
print(currency)
