import openpyxl
import requests
import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd


def getBookUrlFromWriterUrl(options, driver):
    # Collecting Books URL
    booksLinkList = []
    basicUrl = "https://www.rokomari.com"
    empltyBookUrl = 0
    c = {'Books Link': booksLinkList}
    # linkUrlFile = openpyxl.load_workbook('H:\Programming\pyCharm\WebScrappingPython\AllWriterValidUrl_Part_1.xlsx', data_only=True)
    linkUrlFile = openpyxl.load_workbook(r'C:\Users\EATL\PycharmProjects\WebScapping\AllWriterValidUrl_Part_1.xlsx', data_only=True)
    sheet_obj = linkUrlFile.active
    m_row = sheet_obj.max_row
    print(m_row)

    for i in range(18887, m_row):
        cell_obj = sheet_obj.cell(row=i, column=2)
        linkAddress = cell_obj.value
        isNextPresent = True
        while isNextPresent:
            print("Writer Url Link : ", (i - 2))
            print(linkAddress)
            driver.get(linkAddress)
            content = driver.page_source
            soup = BeautifulSoup(content, features="html.parser")
            LinkListDiv = soup.find_all('div', attrs={'class': 'book-list-wrapper'})

            print("Book List from the Writer Url : ")
            # print(LinkListDiv)
            if len(LinkListDiv) > 0:
                # print("Entered into if cond")
                for listTemp in LinkListDiv:
                    aTag = listTemp.find('a')
                    href = aTag.get('href')
                    print(href)
                    booksLinkList.append(basicUrl + href)
                    try:
                        my_element = driver.find_element_by_xpath("//a[text()='next']")
                        # print(my_element.get_attribute('href'))
                        linkAddress = my_element.get_attribute('href')
                    except NoSuchElementException:
                        isNextPresent = False
                        # print("End of Writer Book List")
            else:
                i = i + 1
                cell_obj = sheet_obj.cell(row=i, column=2)
                linkAddress = cell_obj.value
                empltyBookUrl = empltyBookUrl + 1

        print("Empty Book Url Number :", empltyBookUrl)
        # Inserting into Excel File
        df = pd.DataFrame.from_dict(c, orient='index')
        df = df.transpose()
        # df.to_excel(r'H:\Programming\pyCharm\WebScrappingPython\AllBook.xlsx', index=True, encoding='utf-8')
        df.to_excel(r'C:\Users\EATL\PycharmProjects\WebScapping\AllBook.xlsx', index=True, encoding='utf-8')
