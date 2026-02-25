from pages.w3alert import W3Alert
from time import sleep
import pytest
def test_alert(driver):
    w3 = W3Alert(driver)
    w3.open()
    w3.clickBtn()
    assert "cheese" in w3.getTextFromAlert()
    w3.accept_alert()