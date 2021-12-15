from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage():
    def enter_email_address(driver, emailAddress):
        driver.find_element(By.ID, "validateEmail").click()
        driver.find_element(By.ID, "validateEmail").clear()
        driver.find_element(By.ID, "validateEmail").send_keys(emailAddress)
        driver.find_element(By.ID, "validateForm").submit()
        #driver.find_element(By.ID, "validateAccountButton").click()

    def enter_password(driver, password):
        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "password").send_keys()
        driver.find_element(By.CSS_SELECTOR, "#loginAndCheckoutButton > div.text").click()








