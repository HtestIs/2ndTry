from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
class DemoQA(BasePage):
    # IFRAME1 = (By.XPATH,"/html/body/main/div/div[4]/div/iframe")
    IFRAME1 = (By.ID, "my-iframe")
    HEADING = (By.CSS_SELECTOR,"#content > p:nth-child(1)")
    HEADING_OUTSIDE = (By.CSS_SELECTOR,"body > div.trytopnav > div")
    def open(self):
        self.url("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
    def get_text_from_iframe(self):
        self.switch_default()
        self.switch_frame(self.IFRAME1)
        return self.find(self.HEADING).text
    def get_text_from_outside(self):
        self.switch_default()
        # self.wait_presence(self.HEADING_OUTSIDE)
        return self.find(self.HEADING_OUTSIDE).text
    
