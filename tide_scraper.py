"""
A tool to send Seattle tidal data in HTML format through email.
Author: Ivor Zalud
7/1/2019
"""

import requests
import csv
import datetime


def today_date_as_list():
    """
    Creates a list representation of today's shorthand date
    :return:
    """
    full_date = datetime.datetime.now().strftime('%x')
    full_date_split = full_date.split('/')
    full_date_split[2] = datetime.datetime.now().strftime('%Y')
    return full_date_split


def tomorrow_date_as_list():
    """
    Creates a list representation of tomorrows shorthand date
    :return: date as a list
    """
    today = datetime.datetime.now()
    tomorrow = today + datetime.timedelta(days=1)
    tomorrow_full_date = tomorrow.strftime('%x')
    full_date_split = tomorrow_full_date.split('/')
    full_date_split[2] = tomorrow.strftime('%Y')
    return full_date_split


def link_to_csv(link):
    """
    Downloads the CSV from the given link, saves it as a CSV file, and creates a list of the CSV items
    :param link: the csv link
    :return: a list version of the CSV
    """
    with requests.Session() as s:
        download = s.get(link)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines())
        csv_as_list = list(cr)
        # Get the date
        full_date = datetime.datetime.now().strftime('%x')
        full_date_split = full_date.split('/')
        with open(full_date_split[0]+'.'+full_date_split[1]+'.'+full_date_split[2]+'_tides.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(csv_as_list)
        return csv_as_list


def noaa_current_csv_link():
    """
    Creates the csv link to the NOAA site for the current date
    :return: returns the full csv link
    """
    seattle_tide_base_link = 'https://tidesandcurrents.noaa.gov/api/datagetter?product=predictions&application=NOS.' \
                             'COOPS.TAC.WL&'
    seattle_tide_end_link = '&datum=MLLW&station=9447130&time_zone=lst_ldt&units=english&interval=hilo&format=csv'
    today_date_list = today_date_as_list()
    tomorrow_date_list = tomorrow_date_as_list()
    seattle_tide_begin_date = 'begin_date=' + today_date_list[2] + today_date_list[0] + today_date_list[1]
    seattle_tide_end_date = 'end_date=' + tomorrow_date_list[2] + tomorrow_date_list[0]+tomorrow_date_list[1]
    master_link = seattle_tide_base_link+seattle_tide_begin_date+'&'+seattle_tide_end_date+seattle_tide_end_link
    return master_link

# TODO: parse data
# TODO: Send data in an email
# TODO: Set script to run once a day at a certain time
