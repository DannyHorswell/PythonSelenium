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
        time.sleep(2)
        driver.find_element(By.XPATH, "//div[@class='recaptcha-checkbox-border']").click()
        time.sleep(5)
        driver.switch_to.parent_frame()
        driver.find_element(By.CSS_SELECTOR, "#createAccountButton > .text").click()
        self.assertFalse(driver.page_source.__contains__("Sign In"))
    
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
