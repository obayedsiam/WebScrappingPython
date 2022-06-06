import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd

# Preparing chrome for scrapping
options = selenium.webdriver.ChromeOptions()
options.add_argument('--window-size=1920x1080')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# All Store variables
allReviewList = []  # Array of reviews
allReviewerName = []  # Array of Reviewers' Name
allReviewDate = []  # Array of review Date
allBookName = []  # Array of reviewed book name
allBookWriterName = []  # Array of book writers' name
allBookUrlLink = []  # Array of URL Link

# Getting http page from the url
driver.get("https://www.rokomari.com/book/226821/ebar-bhinno-kichu-hok?ref=fl2_p4")
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")

# Finding all the review lists
reviewList = soup.find_all('p', attrs={'class': 'review-text js--review-content'})

# Loop to get all information from single review of all the reviews
for singleReview in reviewList:
    nameOfTheBook = driver.find_element_by_xpath("//div[@class='details-book-main-info__header']/h1").get_attribute(
        'innerHTML')

nameOfTheBookWriter = driver.find_element_by_xpath(
    "//p[@class='details-book-info__content-author']").get_attribute('innerHTML')

for link in soup.find_all('a', attrs={'class': 'review-text js--review-content'}):
    name = link.append(link.get('href'))

nameOfTheReviewer = driver.find_element_by_xpath("//p[@class='d-inline-block name']").get_attribute(
    'innerHTML')
dateOfReview = soup.find('p', attrs={'class': 'date d-inline-block'})

allBookName.append(nameOfTheBook)
allReviewList.append(singleReview.text)
allReviewerName.append(nameOfTheReviewer)
allReviewDate.append(dateOfReview.text)
allBookWriterName.append(nameOfTheBookWriter)

df = pd.DataFrame({'Book Name': allBookName,
                   'Book Writer': allBookWriterName,
                   'Reviewer Name': allReviewerName,
                   'Review Date': allReviewDate,
                   'Review': allReviewList
                   })
df.to_excel(r'C:\Users\EATL\PycharmProjects\WebScapping\products.xlsx', index=True, encoding='utf-8')

print(singleReview.text)
print(nameOfTheReviewer)
print(dateOfReview.text)
print(name)
print(nameOfTheBook)
print(nameOfTheBookWriter)
print("\n")

# bookName = soup.find_all('div', attrs={'class': 'details-book-main-info__header'})
# This is a sample Python script.

# for a in soup.findAll('a', href=True, attrs={'class': '_31qSD5'}):
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

# products = []  # List to store name of the product
# review = []  # List to store price of the product
# # ratings = []  # List to store rating of the product
#
# # driver.get("<a href=https://www.flipkart.com/laptops/")
#
# driver.get("<a href=https://www.rokomari.com/book/226821/ebar-bhinno-kichu-hok?ref=fl2_p4")
