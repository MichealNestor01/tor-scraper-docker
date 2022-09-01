# This file is used by run.sh to check if the tor browser has been connected yet
from modules.getDriver import getDriver

try:
    driver = getDriver()
    driver.get("https://check.torproject.org")
except:
    exit(1)
exit(0)

