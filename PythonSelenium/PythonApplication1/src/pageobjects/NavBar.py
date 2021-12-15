from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NavBar():
    def navigate_to_login(driver):
        driver.find_element(By.CSS_SELECTOR, "button.cookieMessage__button.btn.btn-primary").click()
        driver.find_element(By.CSS_SELECTOR, "a.ico-user.paws-ico.paws-loaded").click()
        driver.find_element(By.ID, "signin").click()

    def navigate_to_favoriates(driver):
        driver.find_element(By.CLASS_NAME, "ico-favourite").click()

    def navigate_to_basket(driver):
        driver.find_element(By.CLASS_NAME, "ico-basket").click()

    def add_text_to_search(driver, search_text):
        driver.find_element(By.CLASS_NAME, "search-input").clear()
        driver.find_element(By.CLASS_NAME, "search-input").send_keys(search_text)
        element = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "//*[@class='product-matches'][contains(@style, 'display: block;')]"))
        )


        

