#!/usr/bin/env python2

from bs4 import BeautifulSoup
from urllib2 import urlopen as Open
import csv
import json

def scrape_process(url):
    response = Open(url)
    soup = BeautifulSoup(response.read(), 'lxml')
    return soup

def main():
    # This url uses latin-1 encoding
    URL = 'https://www.cbssports.com/nfl/stats/playersort/nfl/year-2018-season-regular-category-touchdowns'

    raw_html = scrape_process(URL)
    data_table = raw_html.find('table', class_='data')
    player_info = data_table.find_all('tr')

    for tr in player_info:
        print tr.prettify()

if __name__ == '__main__':
    main()