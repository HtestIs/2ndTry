from pages.dynamic_loading import Dynamic_Loading
import pytest

def test_dylo(driver):
    dylo = Dynamic_Loading(driver)
    dylo.openURL()
    assert "Hello World" in dylo.getText()
def test_dylo2(driver):
    dylo2 = Dynamic_Loading(driver)
    dylo2.openURL2()
    assert "Hello World" in dylo2.getText()