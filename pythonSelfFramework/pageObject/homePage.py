from selenium.webdriver.common.by import By

from pageObject.checkoutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    check = (By.ID, "exampleCheck1")
    gender= (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    successMessage = (By.CSS_SELECTOR, "[class*='alert-success']")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)


    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.check)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)







# from selenium.webdriver.common.by import By
#
# class HomePage:
#     def __init__(self,driver):
#         self.driver = driver
#
#     shop = (By.LINK_TEXT,"Shop")
#     name = (By.CSS_SELECTOR,"input[name='name']")
#     email = (By.NAME, "email")
#     password = (By.ID, "exampleInputPassword1")
#     checkbox  = (By.ID, "exampleCheck1")
#     gender = (By.ID, "exampleFormControlSelect1")
#     submit= (By.XPATH, "//input[@type='submit']")
#     message = (By.CLASS_NAME, "alert-success")
#
#     #self.driver.find_element(By.LINK_TEXT, "Shop").click()
#     def shopitems(self):
#         return self.driver.find_element(*HomePage.shop)
#    # class variable are called by classname.variabl
#     def getName(self):
#         return self.driver.find_element(*HomePage.name)
#     def getemail(self):
#         return self.driver.find_element(*HomePage.email)
#     def getpassword(self):
#         return self.driver.find_element(*HomePage.password)
#     def getcheckbox(self):
#         return self.driver.find_element(*HomePage.checkbox)
#
#     def getgender(self):
#         return self.driver.find_element(*HomePage.gender)
#     def submitform(self):
#         return self.driver.find_element(*HomePage.submit)
#
#     def getsucessmessage(self):
#         return self.driver.find_element(*HomePage.message)
