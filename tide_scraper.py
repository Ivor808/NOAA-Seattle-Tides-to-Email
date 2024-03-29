"""
A tool to send tidal data in HTML format through email.
Author: Ivor Zalud
7/1/2019
"""

import requests
import csv
import datetime
import pandas as pd


class TideScraper:
    def __init__(self, station):
        """
        Default station is Seattle
        """
        self.station = station

    @staticmethod
    def today_date_as_list():
        """
        Creates a list representation of today's shorthand date
        :return:
        """
        full_date = datetime.datetime.now().strftime("%x")
        full_date_split = full_date.split("/")
        full_date_split[2] = datetime.datetime.now().strftime("%Y")
        return full_date_split

    @staticmethod
    def tomorrow_date_as_list():
        """
        Creates a list representation of tomorrows shorthand date
        :return: date as a list
        """
        today = datetime.datetime.now()
        tomorrow = today + datetime.timedelta(days=1)
        tomorrow_full_date = tomorrow.strftime("%x")
        full_date_split = tomorrow_full_date.split("/")
        full_date_split[2] = tomorrow.strftime("%Y")
        return full_date_split

    def link_to_csv(self, link):
        """
        Downloads the CSV from the given link, saves it as a CSV file, and creates a list of the CSV items
        :param link: the csv link
        :return: a list version of the CSV
        """
        with requests.Session() as s:
            download = s.get(link)
            decoded_content = download.content.decode("utf-8")
            cr = csv.reader(decoded_content.splitlines())
            csv_as_list = list(cr)
            with open(TideScraper.csv_file_name(self.station), "w") as csv_file:
                writer = csv.writer(csv_file)
                writer.writerows(csv_as_list)
            return csv_as_list

    def noaa_today_csv_link(self):
        """
        Creates the csv link to the NOAA site for the current date and specified station. If the station is
        blank, then defaults to seattle.
        :return: returns the full csv link
        """
        tide_base_link = (
            "https://tidesandcurrents.noaa.gov/api/datagetter?product=predictions&application=NOS."
            "COOPS.TAC.WL&"
        )
        tide_end_link = "time_zone=lst_ldt&units=english&interval=hilo&format=csv"
        tide_station = "datum=MLLW&station=" + str(self.station) + "&"
        today_date_list = TideScraper.today_date_as_list()
        tomorrow_date_list = TideScraper.tomorrow_date_as_list()
        tide_begin_date = (
            "begin_date=" + today_date_list[2] + today_date_list[0] + today_date_list[1]
        )
        tide_end_date = (
            "end_date="
            + tomorrow_date_list[2]
            + tomorrow_date_list[0]
            + tomorrow_date_list[1]
        )
        master_link = (
            tide_base_link
            + tide_begin_date
            + "&"
            + tide_end_date
            + "&"
            + tide_station
            + tide_end_link
        )
        return master_link

    @staticmethod
    def csv_file_name(station):
        full_date = datetime.datetime.now().strftime("%x")
        full_date_split = full_date.split("/")
        link_name = (
            full_date_split[0]
            + "."
            + full_date_split[1]
            + "."
            + full_date_split[2]
            + "_"
            + str(station)
            + "_tides.csv"
        )
        return link_name

    def csv_to_html(self):
        file_name = TideScraper.csv_file_name(self.station)
        df = pd.read_csv(file_name)
        df.to_html("table.html")

# TODO: Add ability to run indefinetly.
# TODO: Look to have link update at night to be the next day.
