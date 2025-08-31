from locators import MainPageLocators as mpl



# print(tuple(map(lambda x: x.split('x'), mpl.RESOLUTIONS.keys())))
# width, height = map(str().split('x'), tuple(mpl.RESOLUTIONS.keys())).split('x')
# print(f"--windows-size={width},{height}")


#
#
# '''Проверка того, что разрешение экрана в меню разрешения совпадает с разрешением браузера'''
# @pytest.mark.parametrize(
#     "width, height",
#     (
#         (1920, 1080),
#         (2560, 1440),
#         (3840, 2160),
#         (1366, 768),
#         (1280, 720)
#     ))
# def test_info_user_screen(driver_for_screen_test, width, height):
#     driver = driver_for_screen_test(width, height)
#     page = MainPage(driver)
#
#     page.notification_off()
#
#     # page.from_resolutions(None)
#     sleep(2)
#     # Текст разрешения в меню
#     screen_width = page.find_presence_of_element_located(mpl.SCREEN_WIDTH).text
#     print(screen_width)
#     screen_height = page.find_visibility_of_element_located(mpl.SCREEN_HEIGHT).text
#     print(screen_height)
#
#     assert screen_width == width, f"Ширина не совпадает: ожидалось {width}, получено {screen_width}"
#     assert screen_height == height, f"Высота не совпадает: ожидалось {height}, получено {screen_height}"

from allpairspy import AllPairs


def generate_filter_combinations():
    parameters = [
        ["all", "portrait", "landscape"],  # orientation
        ["all", "today", "7days", "30days", "60days"],  # time
        ["latest", "views", "downloads", "favourites", "rating"],  # sort
        ["desc", "asc"]  # order
    ]

    combinations = []
    for i, pairs in enumerate(AllPairs(parameters)):
        combinations.append({
            "orientation": pairs[0],
            "time": pairs[1],
            "sort": pairs[2],
            "order": pairs[3],
            "test_id": f"pair_{i + 1}"
        })
        print(combinations)
    print(len(combinations))
generate_filter_combinations()