#!/usr/bin/env python2

from bs4 import BeautifulSoup
from urllib2 import urlopen as Open
import csv
import json

# This url uses latin-1 encoding
URL = 'https://www.cbssports.com/nfl/stats/playersort/nfl/year-2018-season-regular-category-touchdowns'

def scrape_process(url):
    response = Open(url)
    soup = BeautifulSoup(response.read(), 'lxml')
    return soup

def main():
    players = sou
    test = scrape_process(URL)
    print test.prettify('latin-1')

if __name__ == '__main__':
    main()