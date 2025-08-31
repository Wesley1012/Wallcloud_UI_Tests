import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.ie.service import Service



@pytest.fixture(scope="function")
def driver():
    options = Options()
    # options.add_argument('--headless=new')
    options.add_argument("--start-maximized")
    # options.add_argument("--disable-gpu")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    # options.add_argument("--disable-infobars")

    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")
    service = Service('/home/wesley/PycharmProjects/chromedriver-linux64/chromedriver')

    driver = webdriver.Chrome(options=options, service=service)

    yield driver

    driver.quit()
