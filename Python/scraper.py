"""Module providingFunction scraper web content."""
from bs4 import BeautifulSoup
import requests
# import time
# from selenium.webdriver.support.ui import Select
# from webdriver_manager.chrome import ChromeDriverManager

try:
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/108.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Language': 'en-US,en;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
    }

    # url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"

    response = requests.get(
        "https://rate.bot.com.tw/xrt?Lang=zh-TW", headers=headers, timeout=5)

    if response.status_code == 200:
        html_doc = response.text
        soup = BeautifulSoup(html_doc, 'lxml')
        rate_table = soup.find('table').find('tbody')
        print(rate_table)
        titles = soup.find_all('p', {'class': 'container'})
        result = []
        for title in titles:
            if title:
                result.append(title.getText())
            else:
                print('Element元素不存在')
    else:
        print("回應結果錯誤")

except requests.ConnectionError as conn_ex:
    print(response.text)
    print("連線錯誤")
    print(str(conn_ex))
except requests.Timeout as timeout_ex:
    print("請求超時錯誤")
    print(str(timeout_ex))
except requests.RequestException as request_ex:
    print("請求發生錯誤")
    print(str(request_ex))
except Exception as e:
    print("發生其它錯誤")
    print(str(e))

finally:

    try:
        print(result)
        with open('post.txt', mode='w', encoding=None) as file:
            file.write('\n'.join(result))  # 寫入爬取結果

    except Exception as ex:
        print(str(ex))

        # browser = webdriver.Chrome(ChromeDriverManager().install())
        # browser.get("https://rate.bot.com.tw/xrt?Lang=zh-TW")

        # soup = BeautifulSoup(browser.page_source, "lxml") """
        # print(soup.prettify())  # 輸出排版後的HTML內容

        # https://wms.firstbank.com.tw/main.asp?sUrl=$w$wb$wb01.djhtm?a=jfh02-ja55"
