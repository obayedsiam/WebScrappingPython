import openpyxl
import requests
import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd


def check_empty_url(options, driver):
    # Collecting Books URL
    validUrlList = []
    basicUrl = "https://www.rokomari.com"
    emptyWriterUrl = 0
    d = {'Writer Valid Url': validUrlList}
    # linkUrlFile = openpyxl.load_workbook('H:\Programming\pyCharm\WebScrappingPython\AllWriter.xlsx', data_only=True)
    linkUrlFile = openpyxl.load_workbook(r'C:\Users\EATL\PycharmProjects\WebScapping\AllWriter.xlsx', data_only=True)
    sheet_obj = linkUrlFile.active
    m_row = sheet_obj.max_row
    print(m_row)

    for i in range(61408, m_row):
        cell_obj = sheet_obj.cell(row=i, column=2)
        linkAddress = cell_obj.value
        isNextPresent = True

        print("Writer Url Link : ", (i - 2))
        print(linkAddress)
        driver.get(linkAddress)
        content = driver.page_source
        soup = BeautifulSoup(content, features="html.parser")
        LinkListDiv = soup.find_all('div', attrs={'class': 'book-list-wrapper'})

        # print("Book List from the Writer Url : ")
        # print(LinkListDiv)
        if len(LinkListDiv) > 0:
            # print("Entered into if cond")
            validUrlList.append(linkAddress)
        else:
            # i = i+1
            #         cell_obj = sheet_obj.cell(row=i, column=2)
            #         linkAddress = cell_obj.value
            emptyWriterUrl = emptyWriterUrl+1

        print("Empty Book Url Number :", emptyWriterUrl)
        # Inserting into Excel File
        df = pd.DataFrame.from_dict(d, orient='index')
        df = df.transpose()
        # df.to_excel(r'H:\Programming\pyCharm\WebScrappingPython\AllWriterValidUrl.xlsx', index=True, encoding='utf-8')
        df.to_excel(r'C:\Users\EATL\PycharmProjects\WebScapping\AllWriterValidUrl.xlsx', index=True, encoding='utf-8')
