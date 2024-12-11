"""Module providing Function scraper web (ASP) content to get price of funds."""

from selenium import webdriver
# from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# 打算要取得的基金代碼
fund_list = ['LU0050427557', 'JFCF']

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--window-position=-2400,-2400")
chrome_options.add_argument("--headless=old")
browser = webdriver.Chrome(options=chrome_options)
# browser.implicitly_wait(10)
for fund in fund_list:
    query_url = f'https://announce.fundclear.com.tw/MOPSFundWeb/A01_11.jsp?fundId={fund}'
    print(query_url)

    browser.get(query_url)
    html_doc = browser.page_source
    # print(html_doc)
    soup = BeautifulSoup(html_doc, 'lxml')
    #with open('post.txt', 'w', encoding='utf-8',) as file:
    #    file.write(soup.prettify())

    foundname = soup.find('td', {'class': 'componentTitle'}).get_text()
    titles = soup.find('tr', {'class': 'row1'}).get_text()

    print(foundname)
    print(titles)

"""
result = []
for title in titles:
    if title:
        result.append(title.getText())
    else:
        print('Element元素不存在')
"""
browser.quit()