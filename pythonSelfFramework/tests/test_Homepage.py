
from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest

from TestData.homePagedata import HomePageData
from pageObject.homePage import HomePage
from utility.baseClass import BaseClass


class TestHomePage(BaseClass):
    def test_formSubmission(self,getData):
        log = self.getLogger()
        homepage= HomePage(self.driver)
        log.info("first name is "+getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(), getData["gender"])

        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert ("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         N
        # driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Anju")  # css
        # driver.find_element(By.NAME, "email").send_keys("anju@gmail.com")
        # driver.find_element(By.ID, "exampleInputPassword1").send_keys("1234")
        # driver.find_element(By.ID, "exampleCheck1").click()
        # driver.find_element(By.CSS_SELECTOR, '#inlineRadio1').click()
        # # static dropdown --class select()
        # dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
        # dropdown.select_by_index(0)
        # dropdown.select_by_visible_text("Female")
        # # --custom xpath---//tagnamne[@attribute='Value']===> //input[@type='submit']
        # # --custom Css__ tagnamne[attribute='Value']===> input[type='submit']  , #id  , .class name
        # driver.find_element(By.XPATH, "//input[@type='submit']").click()
        # message = driver.find_element(By.CLASS_NAME, "alert-success").text
        # print(message)
        # assert "Success" in message
        # driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("ANJU")
        # driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()