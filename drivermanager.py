from selenium import webdriver

class DriverManager:
    def get_driver(self):
        browser = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options = browser)
        driver.implicitly_wait(5)
        return driver