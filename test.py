import unittest
from bs4 import BeautifulSoup
import tide_scraper


class MyTestCase(unittest.TestCase):
    def test_link_to_csv_to_list(self):
        isinstance(tide_scraper.link_to_csv(tide_scraper.seattle_tide_csv_link), list)


if __name__ == "__main__":
    unittest.main()
