# scrapeURL.py
# this is the main function that orchestrates the webscraping
from datetime import datetime

from modules.getDriver import getDriver
from modules.scrapeData import scrapeData
from modules.createFileStructure import createFileStructure
from modules.returnCodes import *


# This function actually performes the webscraping of a url
def scrapeURL(url, title, showoutput=True):
    with open("/root/shared-area/log.txt", "a") as file:
        file.write(f"Scrapping data from {url} | {datetime.now()}\n")
        driver = getDriver()
        try: 
            driver.get(url)
        except:
            print(f"ERROR: UNABLE TO REACH {url}")        
            file.write(f"Failed with message: ERROR: UNABLE TO REACH {url} | {datetime.now()}\n")
            return URL_ERROR
        # get correct save path:
        path = createFileStructure()
        # scrape the html data 
        path = scrapeData(driver.page_source, url, title, path)
        # save a screenshot from the website
        driver.save_full_page_screenshot(f"{path}/{title}" + ".png")
        driver.quit()
        if showoutput:
            print(f"Succesfully Scraped: {title}\n\tSource code saved to {path}/{url}.html\n\tScreenshot saved to ./{path}/{url}.png")
        file.write(f"Succesfully Scraped: {title} | {datetime.now()}\n")
        return NO_ERROR

