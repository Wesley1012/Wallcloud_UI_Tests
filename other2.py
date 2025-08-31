from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.ie.service import Service
from locators import MainPageLocators as mpl
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


# RESOLUTIONS = {
#         "1600x1200": (By.XPATH, '//li[@data-size="1600x1200"]')}
#
# def get_res(res):
#     width = res[0].split('x')[0]
#     height = res[0].split('x')[1]
#     print(f'{width}x{height}')
#
# get_res(RESOLUTIONS)
# def get_res(res_dict):
#     # Получаем первый ключ из словаря
#     resolution_str = list(res_dict.keys())[0]
#     # Разбиваем строку по символу 'x'
#     width, height = resolution_str.split('x')
#     print(f'Width: {width}, Height: {height}')
#     return int(width), int(height)

# get_res(RESOLUTIONS)
# print(mpl.RESOLUTIONS.items())
# size, _ = mpl.RESOLUTIONS.items()
res = (
        (1920, 1080),
        (2560, 1440),
        (3840, 2160),
        (1366, 768),
        (1280, 720)
    )
width, height = 2560, 1440
print(width, height)
# options = Options()
# options.add_argument(f"--windows-size={width},{height}")
# options.add_argument("--start-normal")
# options.add_argument("--disable-notifications")
# options.add_argument("--disable-popup-blocking")

service = Service('/home/wesley/PycharmProjects/chromedriver-linux64/chromedriver')


# 1. ЖЕСТКО отключаем максимизацию
chrome_options = Options()
chrome_options.add_argument(f"--window-size={width},{height}")
chrome_options.add_argument("--start-in-normal-mode")  # Ключевой аргумент!
chrome_options.add_argument("--disable-maximized-mode")
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")

# 2. Запускаем драйвер
driver = webdriver.Chrome(options=chrome_options)

# 3. ЧЕРЕЗ JAVASCRIPT (гарантированно работает)
driver.execute_script("window.moveTo(0, 0); window.resizeTo(1280, 720);")
driver.get("https://wallscloud.net/ru/")
# driver.set_window_rect(1280, 720)
wait = WebDriverWait(driver, timeout=10)

not_btn = wait.until(EC.element_to_be_clickable(mpl.NOTIFICATION_BTN)).click()
sleep(1)

res_btn = wait.until(EC.presence_of_element_located(mpl.HEADER['Resolutions List'])).click()
sleep(1)
wi = driver.find_element(By.XPATH, '//span[@class="screen screen_width"]').text
he = driver.find_element(By.XPATH, '//span[@class="screen screen_height"]').text
print(wi, width ,he , height)
# assert  wi == width
# assert  he == height