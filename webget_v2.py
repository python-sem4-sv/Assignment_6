import argparse
import urllib.request as req
from urllib.parse import urlparse
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download a website by giving the URL")
    parser.add_argument("url", help="Add the url to be downloaded")
    args = parser.parse_args()
    url = args.url
    
    parser.add_argument("-d","--destination", help="Add the filepath to where the file should be stored", default='./{}'.format(os.path.basename(url)))
    args = parser.parse_args()
    destination = args.destination


    print("Downloading.. ")
    urlInfo = req.urlretrieve(url, destination)


    