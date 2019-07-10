import tide_scraper


def main():
    tide = tide_scraper.TideScraper()

    tide.link_to_csv(tide.noaa_today_csv_link())


main()
