import pytest
from drivermanager import DriverManager

@pytest.fixture
def driver():
    dm = DriverManager()
    driver = dm.get_driver()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            driver.save_screenshot("failure.png")