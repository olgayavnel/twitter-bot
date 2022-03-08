from selenium import webdriver
from selenium import common
from selenium.webdriver.common.keys import Keys
import time

'''
Twitter Bot
Functionality:
    - login
    - logout
    - accept cookies
    - search
    - like tweets
    - post tweets
    - tear down (or exist the browser)
'''


class TwitterBot():
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()
        self.is_logged_in = False

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(3)

        try:
            url = '/login'
            bot.find_element_by_xpath(
                '//a[@href="' + url + '"]').click()
            print("Log In Button Clicked")
            time.sleep(3)
        except common.exceptions.NoSuchElementException:
            time.sleep(3)
            self.tearDown()

        try:
            email = bot.find_element_by_xpath(
                '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input')
            email.clear()
            email.send_keys(self.username)
            email.send_keys(Keys.RETURN)
            time.sleep(3)
        except common.exceptions.NoSuchElementException:
            time.sleep(3)
            self.tearDown()

        try:
            password = bot.find_element_by_xpath(
                '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            password.clear()
            password.send_keys(self.password)
            password.send_keys(Keys.RETURN)
            time.sleep(3)
        except common.exceptions.NoSuchElementException:
            time.sleep(3)
            self.tearDown()

        self.is_logged_in = True

    def logout(self):
        if not self.is_logged_in:
            return

        bot = self.bot
        bot.get('https://twitter.com/home')
        time.sleep(4)

        try:
            bot.find_element_by_xpath(
                "//div[@data-testid='SideNav_AccountSwitcher_Button']").click()
        except common.exceptions.NoSuchElementException:
            time.sleep(3)
            bot.find_element_by_xpath(
                "//div[@data-testid='SideNav_AccountSwitcher_Button']").click()

        time.sleep(1)

        try:
            bot.find_element_by_xpath(
                "//a[@data-testid='AccountSwitcher_Logout_Button']").click()
        except common.exceptions.NoSuchElementException:
            time.sleep(2)
            bot.find_element_by_xpath(
                "//a[@data-testid='AccountSwitcher_Logout_Button']").click()

        time.sleep(3)

        try:
            bot.find_element_by_xpath(
                "//div[@data-testid='confirmationSheetConfirm']").click()
        except common.exceptions.NoSuchElementException:
            time.sleep(3)
            bot.find_element_by_xpath(
                "//div[@data-testid='confirmationSheetConfirm']").click()

        time.sleep(3)
        self.is_logged_in = False

    def accept_cookies(self):
        if not self.is_logged_in:
            raise Exception("You must log in first!")

        bot = self.bot
        bot.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/div[1]").click()
        print("cookies accepted")
        time.sleep(3)

    def search(self, query=''):
        if not self.is_logged_in:
            raise Exception("You must log in first!")

        bot = self.bot

        try:
            search = bot.find_element_by_xpath(
                "//input[@data-testid='SearchBox_Search_Input']")
            print("searched for webdev")
        except common.exceptions.NoSuchElementException:
            time.sleep(2)
            search = bot.find_element_by_xpath(
                "//input[@data-testid='SearchBox_Search_Input']")
        search.clear()
        search.send_keys(query)
        search.send_keys(Keys.RETURN)
        time.sleep(10)

    def like_tweets(self):
        if not self.is_logged_in:
            raise Exception("You must log in first!")

        bot = self.bot

        for i in range(1, 5):

            liked_element = bot.find_element_by_xpath(
                "//div[@data-testid='unlike']")
            if liked_element:
                pass
                print("Already liked")

            element = bot.find_element_by_xpath("//div[@data-testid='like']")
            print(element)
            try:
                bot.execute_script(
                    "var ele = arguments[0];ele.addEventListener('click', function() {ele.setAttribute('automationTrack','true');});", element)
                element.click()
                print(element.get_attribute("automationTrack"))
            except common.exceptions.NoSuchElementException:
                time.sleep(5)
                bot.execute_script(
                    'window.scrollTo(0,document.body.scrollHeight)')
                time.sleep(5)
                element.click()

            time.sleep(2)
            # first would be zero because we don't have a horizontal scroll.
            # second would be a value, because we have a Y-axis scroll.
            bot.execute_script(
                'window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(5)

    def post_tweets(self, tweet):
        if not self.is_logged_in:
            raise Exception("You must log in first!")

        bot = self.bot

        try:
            bot.find_element_by_xpath(
                "//a[@data-testid='SideNav_NewTweet_Button']").click()
        except common.exceptions.NoSuchElementException:
            time.sleep(3)
            bot.find_element_by_xpath(
                "//a[@data-testid='SideNav_NewTweet_Button']").click()

        time.sleep(3)
        body = tweet

        try:
            bot.find_element_by_xpath("//div[@role='textbox']").send_keys(body)
        except common.exceptions.NoSuchElementException:
            time.sleep(3)
            bot.find_element_by_xpath("//div[@role='textbox']").send_keys(body)

        time.sleep(3)
        bot.find_element_by_class_name(
            "notranslate").send_keys(Keys.ENTER)
        bot.find_element_by_xpath("//div[@data-testid='tweetButton']").click()
        time.sleep(3)

    def tearDown(self):
        self.bot.close()


'''Test Data'''

olga = TwitterBot('', '')
olga.login()
olga.accept_cookies()
olga.search('webdevelopment')
olga.like_tweets()
olga.post_tweets("Hello everyone!")
olga.logout()
olga.tearDown()
