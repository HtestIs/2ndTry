from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
    def wait_visible(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
    def wait_clickable(self,locator):
        self.wait.until(EC.element_to_be_clickable(locator))
    def url(self, url):
        self.driver.get(url)
        self.driver.page_source
    def find(self,locator):
        return self.driver.find_element(*locator)
    def click(self,locator):
        self.wait_clickable(locator)
        self.find(locator).click()
    def type_text(self,locator,text):
        self.wait_visible(locator)
        self.find(locator).send_keys(text)
    def clear(self,locator):
        self.find(locator).clear()
    def get_current_url(self):
        return self.driver.current_url
    def wait_url_contains(self,text):
        self.wait.until(EC.url_contains(text))
    def wait_alert(self):
        self.wait.until(EC.alert_is_present())
        return self.driver.switch_to.alert
    def accept_alert(self):
        alert = self.wait_alert()
        alert.accept()
    def getTextFromAlert(self):
        alert = self.wait_alert()
        return alert.text
    def wait_presence(self,locator):
        self.wait.until(EC.presence_of_element_located(locator))
    def switch_frame(self,locator):
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(locator))