# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
# from urllib.request import urlopen
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#     url = "http://olympus.realpython.org/profiles/aphrodite"
#     page = urlopen(url)
#     html_bytes = page.read()
#     html = html_bytes.decode("utf-8")
#
#     print(html)
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd

options = selenium.webdriver.ChromeOptions()
# options.add_argument('--headless')
# could also do options.headless = True
options.add_argument('--window-size=1920x1080')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.rokomari.com/book/226821/ebar-bhinno-kichu-hok?ref=fl2_p4")

# products = []  # List to store name of the product
# review = []  # List to store price of the product
# # ratings = []  # List to store rating of the product
#
# # driver.get("<a href=https://www.flipkart.com/laptops/")
#
# driver.get("<a href=https://www.rokomari.com/book/226821/ebar-bhinno-kichu-hok?ref=fl2_p4")
#
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")
# for a in soup.findAll('a', href=True, attrs={'class': '_31qSD5'}):
reviewList = soup.find_all('p', attrs={'class': 'review-text js--review-content'})
whole_section = soup.find('div', {'class': "details-book-main-info__header"})
name_person = whole_section.h1.text  # Select person's name, inside "h2" tag.
# time_decease = whole_section.find(lambda element: element.name == 'p' and 'Time of Death:' in element.text)
# for span in time_decease.find('span')
#   span.decompose()

products = []
# bookName = soup.find_all('div', attrs={'class': 'details-book-main-info__header'})

price = driver.find_element_by_xpath("//div[@class='details-book-main-info__header']/h1")
price_content = price.get_attribute('innerHTML')

for a in reviewList:
    # print("hello")
    print(a.text)
    print(name_person)
    print("\n")
    # # name = a.find('div', attrs={'class': '_1vC4OE _2rQ-NK'})
    # # rating = a.find('div', attrs={'class': 'hGSR34 _2beYZw'})
    products.append(a.text)
    # df.to_excel(r'C:\Users\EATL\PycharmProjects\WebScapping\File_Name.xlsx', index=False)

df = pd.DataFrame({'Review': products, 'Book Name': name_person})
df.to_excel(r'C:\Users\EATL\PycharmProjects\WebScapping\products.xlsx', index=True, encoding='utf-8')
