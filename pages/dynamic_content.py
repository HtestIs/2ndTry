from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Dynamic_Content(BasePage):
    URL = "https://the-internet.herokuapp.com/dynamic_content"
    REFRESH = (By.CSS_SELECTOR,"#content > div > p:nth-child(3) > a")
    dyco_text = (By.CSS_SELECTOR,"#content > div:nth-child(7) > div.large-10.columns")
    def open_URL(self):
        self.url(self.URL)
    def get_dyco_text(self):
        return self.find(self.dyco_text).text
    def click_refresh(self):
        self.click(self.REFRESH)