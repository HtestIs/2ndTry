from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Dynamic_Loading(BasePage):
    URL = "https://the-internet.herokuapp.com/dynamic_loading/1"
    URL2 = "https://the-internet.herokuapp.com/dynamic_loading/2"
    LOADING = (By.ID,"loading")
    BUTTON = (By.CSS_SELECTOR,"#start > button")
    FINISH = (By.ID,"finish")
    def openURL(self):
        self.url(self.URL)
    def openURL2(self):
        self.url(self.URL2)
    def getText(self):
        self.click(self.BUTTON)
        self.wait_invisible(self.LOADING)
        self.wait_visible(self.FINISH)
        finish_text = self.find(self.FINISH)
        return finish_text.text

    