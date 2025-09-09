import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.logo_locators import LogoLocators
from pages.base_urls import URLS


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(URLS.BASE_URL)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LogoLocators.scooter_logo)
    )
    yield driver
    driver.quit()