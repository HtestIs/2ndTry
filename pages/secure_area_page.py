from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage

class SecureAreaPage(BasePage):
    SUCCESS_MESSAGE = (By.ID,"flash")

    def get_success_message(self):
        self.wait_visible(self.SUCCESS_MESSAGE)
        return self.find(self.SUCCESS_MESSAGE).text