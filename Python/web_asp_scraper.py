"""Module providingFunction scraper web (ASP) content."""
import os
from selenium import webdriver
# from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument("headless")

os_name = os.name
if os_name=='posix':
    browser = webdriver.Chrome(executable_path='/usr/lib/chromium-browser/chromedriver', chrome_options=options)
else:
    browser = webdriver.Chrome(executable_path='chromedriver', chrome_options=options)
browser.implicitly_wait(10)
browser.get(
    'https://wms.firstbank.com.tw/w/wb/wb01.djhtm?a=jfh02-ja55&amp;openExternalBrowser=1')
print(browser.title)
html_doc = browser.page_source
# print(html_doc)
soup = BeautifulSoup(html_doc, 'lxml')
with open('post.txt', 'w', encoding='utf-8',) as file:
    file.write(soup.prettify())

foundname = soup.find('h1').get_text()

print(foundname)
result = soup.find('ul', {'class': 'stockPanel nav nav-pills list'})

# print(result.select_one("span").get_text())
print(result.select_one("strong").get_text())
print(result.select_one("em").get_text())

data = ["", "", "", "", "", ""]
buff = result.select('span')
ratio = str(buff.copy())
span_number = ratio.count('span class')
index = 1
# start_point = 0
temp_point = 0
for index in range(span_number):
    start_point = ratio.find('>', temp_point)
    end_point = ratio.find('%', temp_point)
    data[index] = ratio[(start_point+1): (end_point+1)]
    temp_point = ratio.find(',', end_point)

print(data)

titles = result.find_all('li')
# result = []
for title in titles:
    print(title.select_one("div").get_text())


"""titles = result.find_all('strong')
for title in titles:
    print(title.select_one("strong").get_text())

titles = result.find_all('em')
for title in titles:
    print(title.select_one("em").get_text())"""

""" titles = result.find_all('span')
print(titles)
for title in titles:
    print(title.select_one('div').get('span class'))"""
#    if li:
#        result.append(price_table.getText())
# foundprice = price_table.__class_getitem__(4)
# print(result)
browser.quit()
