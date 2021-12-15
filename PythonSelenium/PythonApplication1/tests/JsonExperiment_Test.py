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

class Test_Simple2_Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge(service=s, options=options)
        self.driver.maximize_window()
        self.driver.create_options()
        self.driver.implicitly_wait(30)
        self.base_url = "https://sap-sta.paws.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_B(self):

        data = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'

        # Parse JSON into an object with attributes corresponding to dict keys.
        x = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        print(x.name, x.hometown.name, x.hometown.id)



        # Load json from file

        # This loads a json file directly into a new object
        with open('Example.json') as json_file:
            data = json.load(json_file, object_hook=lambda d: SimpleNamespace(**d))

            print(data.name, data.hometown.name, data.hometown.id)


if __name__ == '__main__':
    unittest.main()
