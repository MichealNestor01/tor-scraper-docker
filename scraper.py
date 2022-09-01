# Tor Web Scraper
# python modules
import sys
import os
from datetime import datetime
# our modules
from modules.scrapeURL import scrapeURL
from modules.txtFileHandler import TXTHandler
from modules.csvFileHandler import CSVHandler

# current supported modes and their correspoding functions
MODES = {
    "txt":TXTHandler,
    "url":scrapeURL, #if it is url then the url is given directly
}

# this program is setup to be ran through run.sh
USAGEMESSAGE = "USAGE: \"bash run.sh mode args...\"\nsupported modes:\n\ttxt\n\turl\n"

# main coordinates the program
def main(args):
    with open("./shared-area/log.txt", "a") as file:
        file.write(f"Program started | {datetime.now()}\n")
        # validate args
        if len(args) < 3:
            print(USAGEMESSAGE)
            file.write(f"Program exited with message {USAGEMESSAGE} | {datetime.now()}\n")
            return 0;
        # check that the mode is recognised
        mode = args[1]
        if not (mode in MODES.keys()):
            print(USAGEMESSAGE)
            file.write(f"Program exited with message {USAGEMESSAGE} | {datetime.now()}\n")
            return 0;
        # run the relevant mode's function
    MODES[f"{mode}"](args[2])

if __name__ == "__main__":
    main(sys.argv)

