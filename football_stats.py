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
    # This url uses latin-1 encoding
    URL = 'https://www.cbssports.com/nfl/stats/playersort/nfl/year-2018-season-regular-category-touchdowns'

    raw_html = scrape_process(URL)
    data_table = raw_html.find('table', class_='data')
    player_info = data_table.find_all('tr')
    trimmed_list = player_info[3:23]

    print '\nThe current top 20 players: \n'
    for row in trimmed_list:
        test = row.find_all('td')
        empty_list = []
        for td in test:
            empty_list.append(td)
        print 'Player: {}, Position: {}, Team: {}, Touchdowns: {}'.format(
            empty_list[0].text,
            empty_list[1].text,
            empty_list[2].text,
            empty_list[6].text
        )


if __name__ == '__main__':
    main()
