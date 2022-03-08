from locator import *
from element import BasePageElement


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    def is_title_matches(self):
        return "Twitter" in self.driver.title

    def click_go_button(self):
        # asterix stays for unpacking: *(1,2) = 1 2. It separates the tuple (one object) into arguments (two objects).
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()


class SearchResultPage(BasePage):
    def is_results_found(self):
        return "No results found." not in self.driver.page_source
