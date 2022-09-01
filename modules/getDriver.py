#   getDriver.py 
#   This file returns the selenium web driver needed to for scraping. 
from tbselenium.tbdriver import TorBrowserDriver

def getDriver():
    return TorBrowserDriver("/root/tor-browser_en-US", headless=True, socks_port=9150)