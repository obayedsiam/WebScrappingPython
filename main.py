import openpyxl
import requests
import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
import pandas as pd

import CheckEmptyUrl
import GetBookUrlFromWriter
import GetWriterUrl
import GetData

# file = open("writerUrlNumber.txt", "r")
# writer_url_number = file.read()
# # writer_url_number = type(int(writer_url_number))
# file.close()
# print(writer_url_number)
#
# file = open("writerUrlNumber.txt", "w")
# file.write(1234)
# file.close()

# file = open("writerUrlNumber.txt", "w")
# file.write("4567")
# file.close()

proxies = ["45.152.188.246:3128", "154.13.5.41:59394", "51.250.80.131:80"]

# proxies = GetData.get_free_proxies()
GetData.get_data(proxies, 0)
