import unittest
from selenium import webdriver
import page


class TwitterSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://twitter.com/')

    def test_title(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.click_go_button()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
