import unittest
import json
from types import SimpleNamespace
from collections import namedtuple
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from ConfigFile import config

from src.pageobjects.MainPage import MainPage
from src.pageobjects.LoginPage import LoginPage

CONFIG = config()

s = Service(CONFIG.service)

options = Options()
options.headless = False
options.use_chromium = True

class Login_Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge(service=s, options=options)
        self.driver.maximize_window()
        self.driver.create_options()
        self.driver.implicitly_wait(30)
        self.base_url = "https://sap-sta.paws.com/"
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_unknownEmailsGoesToCreateAccount(self):
        email_prefix = "unknownEmailAddress"
        domain = "@inbox.mailtrap.io"

        driver = self.driver

        driver.get(CONFIG.url)

        MainPage.navigate_to_login(driver)
        LoginPage.enter_email_address(driver, email_prefix + domain)

        self.assertTrue(driver.page_source.__contains__("Create an account"))

    def test_LoginBadPassword(self):

        email_prefix = "705d2182d0-b54e92"
        domain = "@inbox.mailtrap.io"
        password = "badpassword"


        driver = self.driver

        driver.get(CONFIG.url)

        MainPage.navigate_to_login(driver)
        LoginPage.enter_email_address(driver, email_prefix + domain)
        LoginPage.enter_password(driver, password)

        self.assertTrue(driver.page_source.__contains__("Your email address or password was incorrect."))

    def test_CanSignIn(self):

        email_prefix = "705d2182d0-b54e92"
        domain = "@inbox.mailtrap.io"
        password = "S3l3n1umTest$$"


        driver = self.driver

        driver.get(CONFIG.url)

        MainPage.navigate_to_login(driver)
        LoginPage.enter_email_address(driver, email_prefix + domain)
        LoginPage.enter_password(driver, password)

        self.assertFalse(driver.page_source.__contains__("Your email address or password was incorrect."))

if __name__ == '__main__':
    unittest.main()
