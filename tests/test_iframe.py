from pages.iframe_page import DemoQA
from time import sleep
import pytest
def test_alert(driver):
    iframe = DemoQA(driver)
    iframe.open()
    iframe.get_text_from_outside()
    assert "Result Size" in iframe.get_text_from_outside()
    iframe.get_text_from_iframe()
    assert "HTML Iframes" in iframe.get_text_from_iframe()
