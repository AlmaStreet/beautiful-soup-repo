# beautiful-soup-repo
repo for beautiful soup projects

This project was developed to gain hands-on experience scraping data using BeautifulSoup.

The project consists of 3 steps:
1. Get and download webpage data using Python's requests library.
2. Parsing and extracting data values from the response webpage using BeautifulSoup.
3. Saving the data values into excel sheet.

To get started, download book_scraper_improved.py.
pip install openpyxl
pip install requests
pip install bs4

If you are still experiencing import errors:
1. Nagivate to your Python interpreter settings.
2. Under Project, select your Python project.
3. Click the '+' symbol.
4. Search for the imported libraries .
5. Click Install Package.

Once imports are resolved, go ahead and run the Python script.
The script will go to the website: https://www.bookdepository.com/bestsellers?page=333
and extract every available book's Title, Author, Publish date, Price and
save the data in an excel sheet labeled book-depo.xlsx.

Hope you enjoy this!
