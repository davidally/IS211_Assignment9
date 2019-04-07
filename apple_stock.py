#!/usr/bin/env python2

from bs4 import BeautifulSoup
from urllib2 import urlopen as Open
import json
from pprint import pprint


def scrape_process(url):
    response = Open(url)
    soup = BeautifulSoup(response.read(), 'lxml')
    return soup


def main():

    URL = 'https://www.nasdaq.com/symbol/aapl/historical'

    raw_html = scrape_process(URL)
    data_table = raw_html.find(
        id='historicalContainer').find('table').find('tbody').find_all('tr')
    # First row is empty
    trimmed_list = data_table[1:]

    for row in trimmed_list:
        test = row.find_all('td')
        print 'Day: {}, Closing Price: {}'.format(
            test[0].text.strip(),
            test[4].text.strip()
        )


if __name__ == '__main__':
    main()
