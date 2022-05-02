# beautiful-soup-repo
repo for beautiful soup projects

This project was developed to gain hands-on experience scraping data using BeautifulSoup.

The project consists of 3 steps:
1. Get and download webpage data using Python's requests library.
2. Parse and extract data values from the response webpage using BeautifulSoup.
3. Save the data values into an excel sheet.

To get started, download `book_scraper_improved.py` and the libraries below:

```
>>> pip install openpyxl
>>> pip install requests
>>> pip install bs4
```
If you are still experiencing import issues:
1. Nagivate to your Python interpreter settings.
2. Under Project, select your Python project.
3. Click the '+' symbol.
4. Search for the imported libraries.
5. Click Install Package.

Once imports are resolved, go ahead and run the Python script.
The script will go to the website: https://www.bookdepository.com/bestsellers?page=333
and extract every available book's Title, Author, Publish date, Price and
save the data in an excel sheet labeled book-depo.xlsx.

Hope you enjoy this!



Screenshot of book-repo.xlsx

<img width="422" alt="Screen Shot 2022-05-01 at 11 40 23 PM" src="https://user-images.githubusercontent.com/6599619/166194473-53bad70d-49cc-459d-a722-4eb000b756d1.png">
