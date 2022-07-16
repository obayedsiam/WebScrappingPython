import openpyxl
import requests
import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
import CheckEmptyUrl
import GetBookUrlFromWriter
import pandas as pd

options = selenium.webdriver.ChromeOptions()
options.add_argument('--window-size=1920x1080')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


def get_free_proxies():
    url = "https://free-proxy-list.net/"
    # get the HTTP response and construct soup object
    options = selenium.webdriver.ChromeOptions()
    options.add_argument('--window-size=1920x1080')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get(url)
    content = driver.page_source
    soup = bs(requests.get(url).content, "html.parser")
    proxies = []
    for row in soup.find("table", attrs={"class": "table table-striped table-bordered"}).find_all("tr")[1:]:
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            host = f"{ip}:{port}"
            proxies.append(host)
        except IndexError:
            continue

    # df = pd.DataFrame.from_dict(p, orient='index')
    # df = df.transpose()
    # df.to_excel(r'H:\Programming\pyCharm\WebScrappingPython\ValidProxy.xlsx', index=True, encoding='utf-8')
    return proxies


def get_data(proxy_list, proxy_counter):
    options = selenium.webdriver.ChromeOptions()
    options.add_argument('--window-size=1920x1080')
    options.add_argument('--proxy-server=%s' % proxy_list[proxy_counter])
    try:
        # GetWriterUrl.getWriterUrl(options, driver)
        # CheckEmptyUrl.check_empty_url(options, driver)
        GetBookUrlFromWriter.getBookUrlFromWriterUrl(options, driver)
        # GetReviewFromBook.getReview(options, driver)
    except:
        print("New ip needed")
        if (proxy_counter == (len(proxy_list) - 1)) or (proxy_counter == 30):
            print("Existing proxy list ended")
            proxy_list = get_free_proxies()
            get_data(proxy_list, 0)
        else:
            print("Last used proxy list no: ", proxy_counter)
            get_data(proxy_list, proxy_counter + 1)
