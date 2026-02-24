from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.secure_area_page import SecureAreaPage
class Herokyu(BasePage):
    USER_NAME = (By.ID,"username")
    PASSWORD = (By.ID,"password")
    BUTTON = (By.CSS_SELECTOR, "#login > button")
    MESSAGE = (By.ID,"flash")
    def open(self):
        self.url("https://the-internet.herokuapp.com/login")
    def enterUsername(self, text):
        self.type_text(self.USER_NAME,text)
    def enterPassword(self, text):
        self.type_text(self.PASSWORD,text)
    def clickLogin(self):
        self.click(self.BUTTON)
        return SecureAreaPage(self.driver)
    def loginWeb(self, username, password):
        self.enterUsername(username)
        self.enterPassword(password)
        return self.clickLogin()
    def get_error_message(self):
        self.wait_visible(self.MESSAGE)
        return self.find(self.MESSAGE).text
        