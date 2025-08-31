from pages.mainpage import MainPage
from locators import MainPageLocators as mpl
import pytest
from faker import Faker


'''Тесты каждого пункта меню категорий'''
@pytest.mark.parametrize("categori_name, categori_item", mpl.CATEGORIES.items(), ids=tuple(mpl.CATEGORIES.keys()))
def test_categories_items(driver, categori_name, categori_item):
    page = MainPage(driver)

    page.click_menu_and_item(mpl.HEADER['Categories List'], categori_item)

    assert page.current_url() == f'https://wallscloud.net/ru/category/{categori_name.lower()}'

'''Тесты каждого пункта меню разрешений'''
@pytest.mark.parametrize("resolution_name, resolution_item", mpl.RESOLUTIONS.items(), ids=mpl.RESOLUTION_IDS)
def test_resolution_items(driver, resolution_name, resolution_item):
    page = MainPage(driver)

    page.click_menu_and_item(mpl.HEADER['Resolutions List'], resolution_item)

    assert page.current_url() == f'https://wallscloud.net/ru/resolution/{resolution_name.lower()}'

'''Тесты каждого пункта меню топ'''
@pytest.mark.parametrize("top_name, top_item", mpl.TOP_LIST.items(), ids=tuple(mpl.TOP_LIST.keys()))
def test_top_items(driver, top_name, top_item):
    page = MainPage(driver)
    page.click_menu_and_item(mpl.HEADER['Top List'], top_item)

    assert page.current_url() == f'https://wallscloud.net/ru/wallpapers/{top_name.lower()}'

'''Тесты каждого пункта меню 'Ещё' '''
@pytest.mark.parametrize("more_name, more_item", mpl.MORE_LIST.items(), ids=tuple(mpl.MORE_LIST.keys()))
def test_more_items(driver, more_name, more_item):
    page = MainPage(driver)

    page.click_menu_and_item(mpl.HEADER['More List'], more_item)

    if more_name == 'Android_App':
        assert page.current_url() == 'https://wallscloud.net/ru/'
    else:
        assert page.current_url() == f'https://wallscloud.net/ru/{more_name.lower()}'

'''Проверка поля поиска'''
def test_search_bar(driver):
    text = Faker().word()
    page = MainPage(driver)

    page.find_and_send_text(mpl.HEADER['Search Bar'], text)

    assert page.find_presence_of_element_located(mpl.HEADER['Search Button']).is_displayed()

    page.click_element(mpl.HEADER['Search Button'])

    assert page.current_url() == f'https://wallscloud.net/ru/search?q={text}&sort=&color='

'''Проверка кнопки поиска по цвету'''
@pytest.mark.parametrize('color_name, color_locator', mpl.COLORS.items(), ids=tuple(mpl.COLORS.keys()))
def test_color_search(driver, color_name, color_locator):
    page = MainPage(driver)

    page.click_menu_and_item(mpl.HEADER['Color Search'], color_locator)

    # Проверка того что цвет совпадает с выбранной кнопкой
    assert page.find_clickable_of_element_located(mpl.COLOR_VALUE).text == color_name.split(' ')[1]

    page.click_element(mpl.HEADER['Search Button'])

    #Проверка того то значение цвета в параметрах строки передаётся правильно
    assert page.current_url() == f'https://wallscloud.net/ru/search?q=&sort=color&color={color_name.split(' #')[1]}'

'''Проверка кнопки смены языка'''
@pytest.mark.parametrize('lang_name, lang_selector', mpl.LANGUAGE_SELECTORS.items(), ids=tuple(mpl.LANGUAGE_SELECTORS.keys()))
def test_language_switch(driver, lang_name, lang_selector):
    page = MainPage(driver)

    page.change_language(lang_selector)

    assert page.find_clickable_of_element_located(mpl.HEADER['Language Button']).text == lang_name
    assert page.current_url() == f'https://wallscloud.net/{lang_name.lower()}'
    match lang_name:
            case "EN":
                assert page.find_presence_of_element_located(mpl.HEADER['Login Button']).text == 'Guest'
            case "RU":
                assert page.find_presence_of_element_located(mpl.HEADER['Login Button']).text == 'Гость'
            case "UA":
                assert page.find_presence_of_element_located(mpl.HEADER['Login Button']).text == 'Гість'

'''Тесты кнопок login и sing up'''
@pytest.mark.parametrize('item_name, item_selector', mpl.LOGIN_ITEMS.items())
def test_login_button(driver, item_name, item_selector):
    page = MainPage(driver)
    page.click_menu_and_item(mpl.HEADER['Login Button'], item_selector)

    assert page.current_url() == f"https://wallscloud.net/ru/account/{item_name}"




