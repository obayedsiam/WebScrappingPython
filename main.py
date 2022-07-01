import openpyxl
import requests
import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import GetBookUrlFromWriter
import GetReviewFromBook
import GetWriterUrl

# Preparing chrome for scrapping
options = selenium.webdriver.ChromeOptions()
options.add_argument('--window-size=1920x1080')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

#GetWriterUrl.getWriterUrl(options, driver)
GetBookUrlFromWriter.getBookUrlFromWriterUrl(options, driver)
# GetReviewFromBook.getReview(options, driver)



