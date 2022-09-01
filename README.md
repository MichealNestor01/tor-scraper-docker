# Tor Scraper Docker

## Authors: 
-Leonie Kennedy
-Micheal Nestor

## Description
This repository provides a docker image that contains a python program that allows you scrape screenshots and html data from any url including onion sites.

## Setup Instructions
This is a standard docker project. So navigate to the repository and run:
'''
docker build -t Your_Image_Name .  
'''

## Usage Instructions
An option for running: 
'''
docker run --rm -it --entrypoint bash Your_Image_Name
'''
Once in your image, run.sh will be available in root</br>
There are currently two modes, url and txt, with url you pass a single url to scrape and with txt you pass a txt file full of urls to scrape: </br>
'''
bash run.sh url url_to_scrape
'''
'''
bash run.sh txt txt_file_full_of_urls
'''