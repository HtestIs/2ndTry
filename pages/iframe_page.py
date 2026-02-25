from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
class DemoQA(BasePage):
    # IFRAME1 = (By.XPATH,"/html/body/main/div/div[4]/div/iframe")
    IFRAME1 = (By.ID, "iframeResult")
    HEADING = (By.CSS_SELECTOR,"body > h2")
    HEADING_OUTSIDE = (By.CSS_SELECTOR,"body > div.trytopnav > div")
    def open(self):
        self.url("https://seleniumbase.io/w3schools/iframes")
    def get_text_from_iframe(self):
        # print(len(self.find((By.TAG_NAME, "iframe"))))
        self.switch_frame(self.IFRAME1)
        return self.find(self.HEADING).text
    def switch_to_default(self):
        self.driver.switch_to.default_content()
    def get_text_from_outside(self):
        self.switch_to_default()
        # self.wait_presence(self.HEADING_OUTSIDE)
        return self.find(self.HEADING_OUTSIDE).text
    
