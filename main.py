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


from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

products = []  # List to store name of the product
review = []  # List to store price of the product
# ratings = []  # List to store rating of the product

driver.get("<a href=https://www.flipkart.com/laptops/")

driver.get("<a href=https://www.rokomari.com/book/226821/ebar-bhinno-kichu-hok?ref=fl2_p4")

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a', href=True, attrs={'class': '_31qSD5'}):
    name = a.find('div', attrs={'class': 'review-content'})
# name = a.find('div', attrs={'class': '_1vC4OE _2rQ-NK'})
# rating = a.find('div', attrs={'class': 'hGSR34 _2beYZw'})
products.append(name.text)
# prices.append(price.text)
# ratings.append(rating.text)

df = pd.DataFrame({'Reviwer Name': products})
# df = pd.DataFrame({'Reviwer Name': products, 'Price': prices, 'Rating': ratings})
df.to_csv('products.csv', index=False, encoding='utf-8')
