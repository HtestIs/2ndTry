from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
    def wait_visible(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    def url(self, url):
        self.driver.get(url)
    def find(self,locator):
        return self.driver.find_element(*locator)
    def click(self,locator):
        self.wait_visible(locator)
        self.find(locator).click()
    def type_text(self,locator,text):
        self.wait_visible(locator)
        self.find(locator).send_keys(text)
    def clear(self,locator):
        self.find(locator).clear()
