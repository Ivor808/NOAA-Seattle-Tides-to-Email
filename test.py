import unittest
from bs4 import BeautifulSoup
import tide_scraper


class MyTestCase(unittest.TestCase):
    def test_web_object(self):
        x = tide_scraper.web_object(tide_scraper.seattle_tide_link)
        self.assertIsInstance(x, BeautifulSoup)


if __name__ == '__main__':
    unittest.main()
