from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
class SecureAreaPage(BasePage):
    SUCCESS_MESSAGE = (By.ID,"flash")
    LOGOUT_BUTTON = (By.CSS_SELECTOR,"#content > div > a")
    def get_success_message(self):
        self.wait_visible(self.SUCCESS_MESSAGE)
        self.wait_url_contains("secure")
        return self.find(self.SUCCESS_MESSAGE).text
    def click_logout(self):
        from pages.login import Herokyu
        self.click(self.LOGOUT_BUTTON)
        return Herokyu(self.driver)