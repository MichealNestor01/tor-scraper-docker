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
Set up the container from the image: 
'''
docker run -v /path/to/shared/directory/shared-area/:/root/shared-area -d --name Your_Container_Name Your_Image_Name
'''
Access the running container:
'''
docker exec -it Your-Container-Name /bin/bash 
'''
Once in your image, run.sh will be available in root</br>
There are currently two modes, url and txt, with url you pass a single url to scrape and with txt you pass a txt file full of urls to scrape, if you place your text file in the local shared area you can run the program as so: </br>
'''
bash run.sh url url_to_scrape
'''
'''
bash run.sh txt ./shared-area/txt_file_full_of_urls
'''