# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObject.homePage import HomePage
from pageObject.checkoutPage import CheckOutPage
from utility.baseClass import BaseClass


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        homepage.shopitems().click()
        checkoutpage = CheckOutPage(self.driver)
        products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        # products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()
        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        self.driver.find_element(By.XPATH, "//button[@Class='btn btn-success']").click()
        self.driver.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys("ind")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        successMessage = self.driver.find_element(By.CLASS_NAME, "alert-dismissible").text
        assert "Success! Thank you!" in successMessage

