from pages.basepage import BasePage
from locators import MainPageLocators as mpl
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        self.url = "https://wallscloud.net/ru/"
        driver.get(self.url)
        self.wait.until(EC.element_to_be_clickable(mpl.NOTIFICATION_BTN)).click()


    def click_menu_and_item(self, menu, item):
        self.find_visibility_of_element_located(menu).click()
        if item is not None:
            self.find_visibility_of_element_located(item).click()

    def change_language(self, language):
        self.find_visibility_of_element_located(mpl.HEADER['Language Button']).click()
        self.find_visibility_of_element_located(language).click()





