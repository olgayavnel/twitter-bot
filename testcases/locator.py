from selenium.webdriver.common.by import By


class MainPageLocators(object):
    url = '/login'
    GO_BUTTON = (By.XPATH,
                 '//a[@href="' + url + '"]')


class SearchResultsPageLocators(object):
    pass
