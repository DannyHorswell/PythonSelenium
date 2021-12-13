# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import Select
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


class CreateAccount(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge(service=s, options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "https://sap-sta.paws.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_create_account(self):
        driver = self.driver
        # Label: Test
        # ERROR: Caught exception [ERROR: Unsupported command [resizeWindow | 1280,681 | ]]
        driver.get("https://sap-sta.paws.com/")
        driver.find_element(By.CSS_SELECTOR, "button.cookieMessage__button.btn.btn-primary").click()
        driver.find_element(By.CSS_SELECTOR, "a.ico-user.paws-ico.paws-loaded").click()
        driver.find_element(By.CSS_SELECTOR, "#register > div.text").click()
        driver.find_element(By.ID, "validateEmail").click()
        driver.find_element(By.ID, "validateEmail").clear()
        driver.find_element(By.ID, "validateEmail").send_keys(email_prefix + date_time + domain)
        driver.find_element(By.ID, "validateAccountButton").click()
        driver.find_element(By.ID, "registerTitle").click()
        Select(driver.find_element(By.ID, "registerTitle")).select_by_index(1)
        driver.find_element(By.ID, "registerFullName").click()
        driver.find_element(By.ID, "registerFullName").clear()
        driver.find_element(By.ID, "registerFullName").send_keys("Selenium Test")
        driver.find_element(By.NAME, "pwd").click()
        driver.find_element(By.NAME, "pwd").clear()
        driver.find_element(By.NAME, "pwd").send_keys("S3l3niumTest$$")
        driver.find_element(By.CSS_SELECTOR, "div.email-offer-request.checkbox-large > label").click()
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@role='presentation']"))
        time.sleep(10)
        driver.find_element(By.XPATH, "//div[@class='recaptcha-checkbox-border']").click()
        time.sleep(5)
        driver.switch_to.parent_frame()
        driver.find_element(By.CSS_SELECTOR, "#createAccountButton > .text").click()
        self.assertFalse(driver.page_source.__contains__("Sign In"))

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
        driver.find_element(By.ID, "address.postalcode").click()
        driver.find_element(By.ID, "address.postalcode").clear()
        driver.find_element(By.ID, "address.postalcode").send_keys("EC1R 3DG")
        driver.find_element(By.ID, "postCodeLookupBtn").click()
        driver.find_element(By.ID, "address-select").click()
        Select(driver.find_element(By.ID, "address-select")).select_by_visible_text("Paws Group Ltd, 15-19 Baker's Row")
        driver.find_element(By.ID, "address.phone").click()
        driver.find_element(By.ID, "address.phone").clear()
        driver.find_element(By.ID, "address.phone").send_keys("01234567890")
        driver.find_element(By.ID, "addressSubmit").click()
        driver.find_element(By.ID, "deliveryInstructions-select").click()
        Select(driver.find_element(By.ID, "deliveryInstructions-select")).select_by_visible_text("Leave in porch")
        driver.find_element(By.ID, "deliveryMethodSubmit").click()
        driver.find_element(By.ID, "lastInTheForm").click()
        driver.find_element(By.ID, "placeOrder").click()
        driver.find_element(By.ID, "creditCardHolder").click()
        driver.find_element(By.ID, "creditCardHolder").clear()
        driver.find_element(By.ID, "creditCardHolder").send_keys("Selenium Test")
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@role='presentation']"))
        time.sleep(5)
        driver.find_element(By.XPATH, "//*[@id='select2-drop']").click()
        driver.find_element(By.ID, "KKNr").click()
        driver.find_element(By.ID, "KKNr").clear()
        driver.find_element(By.ID, "KKNr").send_keys("375000000000007")
        driver.find_element(By.ID, "SSLForm").click()
        driver.find_element(By.ID, "cccvc").click()
        driver.find_element(By.ID, "cccvc").clear()
        driver.find_element(By.NAME, "cccvc").send_keys("123")
        time.sleep(15)
        self.assertTrue(driver.page_source.__contains__("Checkout Successful"))
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
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
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
