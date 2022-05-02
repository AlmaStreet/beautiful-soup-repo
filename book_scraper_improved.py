'''
Applying BeautifulSoup knowledge in a real world setting and project.
Updated version of book_scraper. Same behavior with much lighter
memory usage.

By Jason Chen

inspired by:
https://data36.com/scrape-multiple-web-pages-beautiful-soup-tutorial/
https://www.skillshare.com/classes/Web-Scraping-Essentials-with-Python-Requests-and-BeautifulSoup/1120631453/

webpage scraped:
https://www.bookdepository.com/bestsellers
'''
import openpyxl
import requests
from bs4 import BeautifulSoup

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = "Book Depository"
sheet["A1"] = "Title"
sheet["B1"] = "Author"
sheet["C1"] = "Publish"
sheet["D1"] = "Price"
sheet["E1"] = "Webpage #"
sheet["F1"] = "Book #"


page = 0
book_number = 1

while True:
    print(f"Page: {page}")
    print(f"\tStep 1. Getting page response")
    response = requests.get(
        url=f"https://www.bookdepository.com/bestsellers?page={page}"
    )
    if not response.ok:
        break

    print(f"\tStep 2. Creating Soup object")
    soup = BeautifulSoup(response.content, "html.parser")
    books = soup.find_all("div", class_="item-info")

    # No more books available
    if len(books) < 1:
        print("Ran out of books...")
        break

    print(f"\tStep 3. Extracting book data")
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
        sheet.append([title, author, publish, price, page, book_number])
        book_number += 1
    page += 1

    print(f"\tStep 4. Saving book data")
    # Data is saved every page to ensure data can persist in case of
    # a crash and data can be used while newer data is being saved.
    wb.save("book-depo-1.xlsx")

print(f"Book scraping complete!")

