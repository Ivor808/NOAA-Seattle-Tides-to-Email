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
seattle_tide_link = 'https://tidesandcurrents.noaa.gov/noaatidepredictions.html?id=9447130&legacy=11'
seattle_tide_csv_link = 'https://tidesandcurrents.noaa.gov/api/datagetter?product=predictions&application=NOS.COOPS.' \
                        'TAC.WL&begin_date=20190702&end_date=20190703&datum=MLLW&station=9447130&time_zone' \
                        '=lst_ldt&units=english&interval=hilo&format=csv'

def web_object(web_link):
    """
    Creates a web object that we can use to pull the data labels from
    :param web_link: the link to scrape
    :return: a beautifulsoup object
    """
    page = requests.get(web_link)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup


with requests.Session() as s:
    download = s.get(seattle_tide_csv_link)
    print(type(download.content))
    decoded_content = download.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines())
    my_list = list(cr)
    for row in my_list:
        print(row)
