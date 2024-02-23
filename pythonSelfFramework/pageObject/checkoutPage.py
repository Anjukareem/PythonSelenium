from selenium.webdriver.common.by import By


class CheckOutPage():
    def __init__(self,driver):
        self.driver = driver
    productTitle=(By.XPATH,"//div[@class='card h-100']")
    productlist=(By.XPATH, "div/h4/a")
    productselect = (By.XPATH, "div/button")
    #products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    def getProductTitles(self):
        return self.driver.find_element(*CheckOutPage.productTitle) # need to use star for tuple extraction

    def getProductlist(self):
        return self.driver.find_element(*CheckOutPage.productlist)
    def getProductselect(self):
        return self.driver.find_element(*CheckOutPage.productselect)