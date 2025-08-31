from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse

class BasePage(object):
    def __init__(self, driver, url=None, timeout=10):
        self.url = url
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    def find_presence_of_element_located(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_visibility_of_element_located(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_invisibility_of_element_located(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def find_clickable_of_element_located(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def current_url(self):
        return self.driver.current_url

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)

    def find_and_send_text(self, locator, text):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        # element.click()
        element.clear()
        element.send_keys(text)
