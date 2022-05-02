'''
Applying BeautifulSoup knowledge in a real world setting and project
By Jason Chen

inspired by:
https://data36.com/scrape-multiple-web-pages-beautiful-soup-tutorial/
https://www.skillshare.com/classes/Web-Scraping-Essentials-with-Python-Requests-and-BeautifulSoup/1120631453/

webpage scraped:
https://www.bookdepository.com/bestsellers
'''
import sys
import logging
import openpyxl
import requests
from bs4 import BeautifulSoup

logger = logging.getLogger()
stream_handler = logging.StreamHandler(sys.stdout)

max_pages = 300
page = 0
soups = []
logging.info("1. Start Page Download")
# Gets and stores all pages into a soup list.
while page < max_pages:
    response = requests.get(
        url=f"https://www.bookdepository.com/bestsellers?page={page}"
    )
    if not response.ok:
        break
    soup = BeautifulSoup(response.content, "html.parser")
    soups.append(soup)
    page += 1
logging.info(f"1.2 Gathered {page} webpages of books")
page = 1
book_lists = {}
logging.info("2. Start Soup Scraping")

# Parse each soup object and extract book's
# title, author, publish date, and price.
for soup in soups:
    books = soup.find_all("div", class_="item-info")
    book_list = []
    logging.info(f"2.1 Parsing page: {page}")

    for book in books:
        try:
            title = book.h3.a.text.strip()
            author = book.find("p", class_="author").a.text.strip()
            publish = book.find("p", class_="published").text.strip()
            price = book.find(
                "div", class_="price-wrap omnibus-experiment-control"
            ).p.span.text.strip()
        except Exception:
            pass
        book_list.append([title, author, publish, price, page])

    book_lists[page] = book_list
    page += 1

# Save All booklists into an excel sheet
print(book_lists)
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = "Book Depository"
sheet["A1"] = "Title"
sheet["B1"] = "Author"
sheet["C1"] = "Publish"
sheet["D1"] = "Price"
sheet["E1"] = "Webpage #"

for book_list_index in book_lists:
    for book_value in book_lists[book_list_index]:
        sheet.append(book_value)

wb.save("book-depo.xlsx")
