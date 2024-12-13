"""Module providing Function scraper web (ASP) content to get price of funds."""

from selenium import webdriver
# from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import numpy as np

# 打算要取得的基金代碼
fund_list = ['LU0050427557', 'JFCF']
fund_data = [[u" ",u" ",u" ", u" ",u" ",u" "], [u" ",u" ",u" ", u" ",u" ",u" "]]

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--window-position=-2400,-2400")
chrome_options.add_argument("--headless=old")
browser = webdriver.Chrome(options=chrome_options)

idx = int(0)
for fund in fund_list:
    query_url = f'https://announce.fundclear.com.tw/MOPSFundWeb/A01_11.jsp?fundId={fund}'
    print(query_url)

    browser.get(query_url)
    browser.implicitly_wait(10)
    html_doc = browser.page_source
    # print(html_doc)
    soup = BeautifulSoup(html_doc, 'lxml')
    #with open('post.txt', 'w', encoding='utf-8',) as file:
    #    file.write(soup.prettify())

    fund_name = soup.find('td', {'class': 'componentTitle'}).get_text()
    price_data = soup.find('tr', {'class': 'row1'}).get_text()

    fund_name = fund_name.split('\n')
    price_data = price_data.split('\n')
    print(fund_name[0])
    print(price_data[1:5])

    fund_data[idx][0] = fund_list[idx]
    fund_data[idx][1] = fund_name[0]
    fund_data[idx][2] = price_data[2]
    fund_data[idx][3] = price_data[1]
    fund_data[idx][4] = float(price_data[2])-float(price_data[4])
    fund_data[idx][5] = (float(price_data[2])-float(price_data[4]))/float(price_data[4])
    idx = idx + 1

print(fund_data)

"""
result = []
for title in titles:
    if title:
        result.append(title.getText())
    else:
        print('Element元素不存在')
"""
browser.quit()