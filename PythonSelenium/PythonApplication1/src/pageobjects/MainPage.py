from selenium import webdriver
from selenium.webdriver.common.by import By

class MainPage():
    def navigate_to_login(driver):
        driver.find_element(By.CSS_SELECTOR, "button.cookieMessage__button.btn.btn-primary").click()
        driver.find_element(By.CSS_SELECTOR, "a.ico-user.paws-ico.paws-loaded").click()
        driver.find_element(By.ID, "signin").click()