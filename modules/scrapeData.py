#   scrapeData.py 
#   This file returns the page title, and saves the sourcecode from a website 
import bs4
import os
from datetime import datetime

# Takes the source code of a given site (driver.page_source)
def scrapeData(html, url, title, path):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    os.mkdir(f"{path}/{title}")
    path = f"{path}/{title}/{str(datetime.now().time())[0:5]}"
    os.mkdir(path)
    with open(f"/{path}/index.html", "w+", encoding="utf-8") as file:
        file.write(html)
    return path

