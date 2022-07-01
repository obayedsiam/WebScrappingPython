import openpyxl
import requests
import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd


def getWriterUrl(options, driver):

    # Collecting writers name
    writerWiseBookLinkList = []
    basicUrl = "https://www.rokomari.com"
    b = {'Writers Book Link': writerWiseBookLinkList}
    authorListPage = "https://www.rokomari.com/book/authors?ref=mm&page=1"
    isNextPresent = True
    while isNextPresent:
        driver.get(authorListPage)
        content = driver.page_source
        soup = BeautifulSoup(content, features="html.parser")
        LinkListUI = soup.find('ul', attrs={'class': 'list-inline list-unstyled authorList'})
        thisPageWriterCount = len(LinkListUI.find_all(recursive=False))
        listLI = LinkListUI.find_all(recursive=False)
        print("####################")
        for listTemp in listLI:
            aTag = listTemp.find('a')
            href = aTag.get('href')
            print(href)
            writerWiseBookLinkList.append(basicUrl + href)
        try:
            my_element = driver.find_element_by_xpath("//a[text()='next ']")
            print(my_element.get_attribute('href'))
            authorListPage = my_element.get_attribute('href')
        except NoSuchElementException:
            isNextPresent = False
            print("Hello")

    # Inserting into Excel File
    df = pd.DataFrame.from_dict(b, orient='index')
    df = df.transpose()
    # df.to_excel(r'C:\Users\EATL\PycharmProjects\WebScapping\AllWriter.xlsx', index=True, encoding='utf-8')
    df.to_excel(r'H:\Programming\pyCharm\WebScrappingPython\AllWriter.xlsx', index=True, encoding='utf-8')
