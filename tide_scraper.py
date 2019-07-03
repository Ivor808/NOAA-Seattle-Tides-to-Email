"""
A tool to send Seattle tidal data in HTML format through email.
Author: Ivor Zalud
7/1/2019
"""

from bs4 import BeautifulSoup
import requests
import urllib
import csv

# Define the link
seattle_tide_csv_link = 'https://tidesandcurrents.noaa.gov/api/datagetter?product=predictions&application=NOS.COOPS.' \
                        'TAC.WL&begin_date=20190702&end_date=20190703&datum=MLLW&station=9447130&time_zone' \
                        '=lst_ldt&units=english&interval=hilo&format=csv'


def link_to_csv(link):
    with requests.Session() as s:
        download = s.get(link)
        print(type(download.content))
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines())
        with open()
        return my_list
