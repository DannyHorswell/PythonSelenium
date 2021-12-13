# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import pytest
import unittest
import datetime
import logging

s = Service("C:\\SeleniumProjects\\WebDrivers\\msedgedriver.exe")
options = Options()
# options.headless = True
# options.use_chromium = True

now = datetime.datetime.now()
date_time = now.strftime("%d-%m-%Y-%H%M")
email_prefix = "705d2182d0-b54e92"
domain = "@inbox.mailtrap.io"


class CheckAccountExists_Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge(service=s, options=options)
        self.driver.maximize_window()
        self.driver.create_options()
        self.driver.implicitly_wait(30)
        self.base_url = "https://sap-sta.paws.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_account_login(self):
        driver = self.driver
        # Label: Test
        # ERROR: Caught exception [ERROR: Unsupported command [resizeWindow | 1280,681 | ]]
        driver.get("https://sap-sta.paws.com/")
        driver.find_element(By.CSS_SELECTOR, "button.cookieMessage__button.btn.btn-primary").click()
        driver.find_element(By.CSS_SELECTOR, "a.ico-user.paws-ico.paws-loaded").click()
        driver.find_element(By.ID, "signin").click()
        driver.find_element(By.ID, "validateEmail").click()
        driver.find_element(By.ID, "validateEmail").clear()
        driver.find_element(By.ID, "validateEmail").send_keys(email_prefix + domain)
        driver.find_element(By.ID, "validateForm").submit()
        driver.find_element(By.ID, "validateAccountButton").click()
        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "password").send_keys("S3l3n1umTest$$")
        driver.find_element(By.CSS_SELECTOR, "#loginAndCheckoutButton > div.text").click()
        self.assertFalse(driver.page_source.__contains__("Your email address or password was incorrect."))

        # Add product to basket
        driver.find_element(By.NAME, "text").click()
        driver.find_element(By.NAME, "text").clear()
        driver.find_element(By.NAME, "text").send_keys("I9527482")
        driver.find_element(By.NAME, "search_form_SearchBox").submit()
        driver.find_element(By.CSS_SELECTOR, "img.img-responsive.js-lazy").click()
        driver.find_element(By.ID, "one-time-option").click()
        driver.find_element(By.ID, "quantity").click()
        Select(driver.find_element(By.ID, "quantity")).select_by_visible_text("2")
        driver.find_element(By.ID, "addToCartButton").click()

        # Checkout
        driver.find_element(By.CSS_SELECTOR, "div.text").click()
        driver.find_element(By.CSS_SELECTOR, "div.default-checkout-option.summary.large-button.light-button > #summarySectionCheckoutButton > div.text").click()
        driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.btn-block.checkout-next").click()
        driver.find_element(By.ID, "deliveryInstructions-select").click()
        Select(driver.find_element(By.ID, "deliveryInstructions-select")).select_by_visible_text("Leave in garage")
        driver.find_element(By.ID, "deliveryMethodSubmit").click()
        driver.find_element(By.ID, "lastInTheForm").click()
        driver.find_element(By.ID, "placeOrder").click()
        time.sleep(5)
        driver.find_element(By.ID, "submit1").click()
        time.sleep(15)
        self.assertTrue(driver.page_source.__contains__("Checkout Successful"))

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
