from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
class Rebuild:
    def setup(self):
        self.browser = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=self.browser)
        self.wait = WebDriverWait(self.driver, 10)
    def solaire(self):
        try:
            self.driver.get("https://www.google.com/")
            search_box = self.wait.until(EC.presence_of_element_located((By.ID,"APjFqb")))
            search_box.send_keys("I love Solaire!!!")
            sleep(5)
        except TimeoutException:
            print("hahaha")
    def exit(self):
        self.driver.quit()

if __name__ == "__main__":
    test = Rebuild()
    test.setup()
    try:
        test.solaire()
    finally:
        test.exit()