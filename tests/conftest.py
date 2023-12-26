import pytest
from selene.support.shared import browser

@pytest.fixture()
def open_browser():
    browser.driver.set_window_size(width=1920, height=1080)
    browser.config.timeout=2
    yield browser
    browser.quit()