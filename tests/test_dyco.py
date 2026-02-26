from pages.dynamic_content import Dynamic_Content
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import pytest

def test_dyco(driver):
    dyco = Dynamic_Content(driver)
    dyco.open_URL()
    # first_content = driver.find_element(By.CSS_SELECTOR,"#content > div:nth-child(7) > div.large-10.columns")
    text_before = dyco.get_dyco_text()
    dyco.click_refresh()
    # print(first_content.text)
    text_after = dyco.get_dyco_text()
    assert text_before != text_after