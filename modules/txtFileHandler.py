# txtFileHandler.py
# this handles reading urls from txt files
from modules.scrapeURL import scrapeURL
from modules.returnCodes import *

import os

def getPageTitle(url):
    title = url[8:len(url)]
    for index, char in enumerate(title):
        if char == '/':
            return title[0:index]
    return title

def TXTHandler(file_name):
    # we have to do this separately, because scrapeURL also opens a text file
    # first get of the urls
    urls = []
    titles = []
    try:
        with open(file_name) as file:
            for url in file.readlines():
                if url[len(url)-1] == "\n":
                    url = url[0:len(url)-1]
                titles.append(getPageTitle(url))
                urls.append(url) # remove line break
    except FileNotFoundError:
        print(f"ERROR: {file_name} NOT FOUND")
    # then scrape the data from the urls
    for index, url in enumerate(urls):
        returnCode = scrapeURL(url, titles[index])
        if returnCode == WEBDRIVER_ERROR:
            return WEBDRIVER_ERROR
