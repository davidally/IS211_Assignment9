#!/usr/bin/env python2

from bs4 import BeautifulSoup
from urllib2 import urlopen as Open


def scrape_process(url):
    """Grabs the raw html from a page and returns it.

    Args:
        url (string): A URL with html to be processed.

    Returns:
        string: Raw HTML data. 
    """

    response = Open(url)
    soup = BeautifulSoup(response.read(), 'lxml')
    return soup


def main():
    # This url uses latin-1 encoding
    URL = 'https://www.cbssports.com/nfl/stats/playersort/nfl/year-2018-season-regular-category-touchdowns'

    raw_html = scrape_process(URL)
    data_table = raw_html.find('table', class_='data').find_all('tr')
    trimmed_list = data_table[3:23]

    print '\nThe current top 20 players: \n'
    for row in trimmed_list:
        row_data = row.find_all('td')
        print 'Player: {}, Position: {}, Team: {}, Touchdowns: {}'.format(
            row_data[0].text,
            row_data[1].text,
            row_data[2].text,
            row_data[6].text
        )


if __name__ == '__main__':
    main()
