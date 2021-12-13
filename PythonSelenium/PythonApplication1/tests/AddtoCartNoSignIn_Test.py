# -*- coding: utf-8 -*-
import selenium.webdriver.edge.options
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException


from ConfigFile import config

import logging
import unittest
import time
import re

CONFIG = config()

s = Service(CONFIG.service)

#s = Service("C:\\SeleniumProjects\\WebDrivers\\msedgedriver.exe")
options = Options()
options.headless = False
options.use_chromium = True


class AddToBasket(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge(service=s, options=options)
        self.driver.implicitly_wait(30)
        self.base_url = "https://sap-sta.paws.com/"
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_add_to_basket(self):
        driver = self.driver
        driver.maximize_window()
        # Label: Test
        # ERROR: Caught exception [ERROR: Unsupported command [resizeWindow | 1280,681 | ]]
        driver.get("https://sap-sta.paws.com/")
        driver.find_element(By.CSS_SELECTOR, "button.cookieMessage__button.btn.btn-primary").click()
        driver.find_element(By.CSS_SELECTOR, "a.primary-nav-link.nav-primary.action-level-1.has-no-url > div.text").click()
        driver.find_element(By.XPATH, "//li/div/ul/li[2]/a/div").click()
        driver.find_element(By.XPATH, "//img[@alt='The Rockster Chickenrella Bio-Organic Chicken Can']").click()
        driver.find_element(By.ID, "one-time-option").click()
        driver.find_element(By.ID, "quantity").click()
        Select(driver.find_element(By.ID, "quantity")).select_by_visible_text("2")
        driver.find_element(By.CSS_SELECTOR, "#addToCartButton > div.text").click()
        driver.find_element(By.CSS_SELECTOR, "a.primary-nav-link.nav-primary.action-level-1.has-no-url > div.text").click()
        driver.find_element(By.XPATH, "//li[2]/a/div[2]").click()
        driver.find_element(By.CSS_SELECTOR, "div.nav-level.nav-level-3.active > div.paws-container.nav-grid.wrap-columns > div.column-1-category > div.nav-category-list.masonry > div.nav-brick > ul > li > div.nav-category-leaves > ul > li > a.category-nav-link.has-url > div.text").click()
        driver.find_element(By.CSS_SELECTOR, "img.img-responsive.js-lazy").click()
        driver.find_element(By.CSS_SELECTOR, "label.radio-button-label > span.text").click()
        driver.find_element(By.CSS_SELECTOR, "#addToCartButton > div.text").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
