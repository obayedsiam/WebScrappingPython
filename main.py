import openpyxl
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

# Array for header
a = {'Book Name': allBookName,
     'Writer Name': allBookWriterName,
     'Reviewer Name': allReviewerName,
     'Review Date': allReviewDate,
     'Review': allReviewList}

linkUrlFile = openpyxl.load_workbook('C:\\Users\\EATL\\PycharmProjects\\WebScapping\\link.xlsx', data_only=True)
sheet_obj = linkUrlFile.active
m_row = sheet_obj.max_row
print(m_row)

for i in range(1, 3):
    cell_obj = sheet_obj.cell(row=i, column=2)
    linkAddress = cell_obj.value
    print(linkAddress)
    # Getting http page from the url
    driver.get(linkAddress)
    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")

    # Finding all the lists
    reviewList = soup.find_all('p', attrs={'class': 'review-text js--review-content'})
    dateOfReviewList = soup.find_all('p', attrs={'class': 'date d-inline-block'})
    nameOfTheReviewer = soup.find_all('p', attrs={'class': 'd-inline-block name'})

    Book = soup.find('div', attrs={'class': 'details-book-main-info__header'})
    Writer = soup.find('p', attrs={'class': 'details-book-info__content-author'})

    # Book Name
    print(Book.text)

    # Writer Name
    print(Writer.find('a').contents[0])

    # Review from List
    for singleReview in reviewList:
        print(singleReview.text)
        allReviewList.append(singleReview.text)
        allBookName.append(Book.text)
        allBookWriterName.append(Writer.find('a').contents[0])

    # Review Date from List
    for singleDate in dateOfReviewList:
        if len(singleDate.text) > 0:
            print(singleDate.text)
            allReviewDate.append(singleDate.text)

    # Reviewer Name from List
    for p in nameOfTheReviewer:
        k = p.text.replace("By ", "")
        k = k.replace(", ", "")
        if len(k) > 0:
            print(k)
            allReviewerName.append(k)

    # Inserting into Excel File
    df = pd.DataFrame.from_dict(a, orient='index')
    df = df.transpose()
    df.to_excel(r'C:\Users\EATL\PycharmProjects\WebScapping\products.xlsx', index=True, encoding='utf-8')
    # df.to_excel(r'H:\Programming\pyCharm\WebScrappingPython\products.xlsx', index=True, encoding='utf-8')

#########################################################################################################
# allBookName.append(nameOfTheBook)
# print(nameOfTheWriter)
# print(nameOfTheBook)
# nameOfTheBookWriter = driver.find_element_by_xpath(
#     "//p[@class='details-book-info__content-author']").get_attribute('innerHTML')
# print(singleReview.text)
# nameOfTheReviewer = driver.find_element_by_xpath("//p[@class='d-inline-block name']/span").get_attribute('innerHTML')
# allReviewerName.append(nameOfTheReviewer.text)
# print(nameOfTheReviewer)
# nameOfTheBook = driver.find_element_by_xpath("//div[@class='details-book-main-info__header']/h1").get_attribute(
#     'innerHTML')

# nameOfTheBookWriter = driver.find_element_by_xpath(
#     "//p[@class='details-book-info__content-author']").get_attribute('innerHTML')
#
# for link in soup.find_all('a', attrs={'class': 'review-text js--review-content'}):
#     name = link.append(link.get('href'))
#


# allBookWriterName.append(nameOfTheBookWriter)
# print(nameOfTheReviewer)
# print("\n")

# print(name)
# print(nameOfTheBook)
# print(nameOfTheBookWriter)


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
