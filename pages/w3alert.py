from selenium.webdriver.common.by import By
from pages.base_page import BasePage
class W3Alert(BasePage):
    BUTTON = (By.ID,"alert")
    def open(self):
        self.url("https://www.selenium.dev/selenium/web/alerts.html")
    def clickBtn(self):
        self.wait_clickable(self.BUTTON)
        self.find(self.BUTTON).click()
        self.wait_alert()