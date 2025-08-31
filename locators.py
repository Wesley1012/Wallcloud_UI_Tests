from selenium.webdriver.common.by import By


class MainPageLocators:

    #Other
    NOTIFICATION_BTN = (By.ID, 'popup-decline-btn')
    SCREEN_WIDTH = (By.XPATH, '//span[@class="screen screen_width"]/text()')
    SCREEN_HEIGHT = (By.XPATH, '//span[@class="screen screen_height"]')

    HEADER = {
        'Logo Icon': (By.CSS_SELECTOR, 'span.logo-icon'),
        'Categories List': (By.ID, 'categories-list'),
        'Resolutions List': (By.ID, 'resolutions-list'),
        'Top List': (By.ID, 'top-list'),
        'Random List': (By.CSS_SELECTOR, 'li.waves.waves-effect.waves-light'),
        'More List': (By.ID, 'more-list'),
        'Search Button': (By.CSS_SELECTOR, 'button.btn.go-search'),
        'Search Bar': (By.NAME, 'q'),
        'Color Search': (By.XPATH, '//div[@class="color_pallet tooltips"]/span[@class="msr"]'),
        'Language Button': (By.XPATH, '//ul[@id="lang_list"]'),
        'Login Button': (By.XPATH, '//li[@class="dropdown m-profile"]//span[@class="user-name"]')
    }

    #Categories List
    CATEGORIES = {
        "3d": (By.XPATH, '//li[@class="3d"]'),
        "Hi-Tech": (By.XPATH, '//li[@class="hi-tech"]'),
        "Weapon": (By.XPATH, '//li[@class="weapon"]'),
        "Abstract": (By.XPATH, '//li[@class="abstract"]'),
        "Aircraft": (By.XPATH, '//li[@class="aircraft"]'),
        "Cars": (By.XPATH, '//li[@class="cars"]'),
        "Anime": (By.XPATH, '//li[@class="anime"]'),
        "Architecture": (By.XPATH, '//li[@class="architecture"]'),
        "Cities": (By.XPATH, '//li[@class="cities"]'),
        "Graphics": (By.XPATH, '//li[@class="graphics"]'),
        "Food": (By.XPATH, '//li[@class="food"]'),
        "Animals": (By.XPATH, '//li[@class="animals"]'),
        "Games": (By.XPATH, '//li[@class="games"]'),
        "Illustration": (By.XPATH, '//li[@class="illustration"]'),
        "Interiors": (By.XPATH, '//li[@class="interiors"]'),
        "Computers": (By.XPATH, '//li[@class="computers"]'),
        "Ships": (By.XPATH, '//li[@class="ships"]'),
        "Space": (By.XPATH, '//li[@class="space"]'),
        "Love": (By.XPATH, '//li[@class="love"]'),
        "People": (By.XPATH, '//li[@class="people"]'),
        "Macro": (By.XPATH, '//li[@class="macro"]'),
        "Minimalism": (By.XPATH, '//li[@class="minimalism"]'),
        "Motorcycles": (By.XPATH, '//li[@class="motorcycles"]'),
        "Music": (By.XPATH, '//li[@class="music"]'),
        "Multiplicatios": (By.XPATH, '//li[@class="multiplicatios"]'),
        "Holidays": (By.XPATH, '//li[@class="holidays"]'),
        "Funny": (By.XPATH, '//li[@class="funny"]'),
        "Nature": (By.XPATH, '//li[@class="nature"]'),
        "Others": (By.XPATH, '//li[@class="others"]'),
        "Sport": (By.XPATH, '//li[@class="sport"]'),
        "Textures": (By.XPATH, '//li[@class="textures"]'),
        "Fantasy": (By.XPATH, '//li[@class="fantasy"]'),
        "Films": (By.XPATH, '//li[@class="films"]')
    }


    # Resolution list
    RESOLUTIONS = {
        "1600x1200": (By.XPATH, '//li[@data-size="1600x1200"]'),
        "1920x1440": (By.XPATH, '//li[@data-size="1920x1440"]'),
        "2560x1920": (By.XPATH, '//li[@data-size="2560x1920"]'),
        "2800x2100": (By.XPATH, '//li[@data-size="2800x2100"]'),
        "3200x2400": (By.XPATH, '//li[@data-size="3200x2400"]'),

        "1280x1024": (By.XPATH, '//li[@data-size="1280x1024"]'),
        "2560x2048": (By.XPATH, '//li[@data-size="2560x2048"]'),

        "1152x720": (By.XPATH, '//li[@data-size="1152x720"]'),
        "1280x800": (By.XPATH, '//li[@data-size="1280x800"]'),
        "1440x900": (By.XPATH, '//li[@data-size="1440x900"]'),
        "1680x1050": (By.XPATH, '//li[@data-size="1680x1050"]'),
        "1920x1200": (By.XPATH, '//li[@data-size="1920x1200"]'),
        "2560x1600": (By.XPATH, '//li[@data-size="2560x1600"]'),
        "2880x1800": (By.XPATH, '//li[@data-size="2880x1800"]'),

        "1024x576": (By.XPATH, '//li[@data-size="1024x576"]'),
        "1280x720": (By.XPATH, '//li[@data-size="1280x720"]'),
        "1366x768": (By.XPATH, '//li[@data-size="1366x768"]'),
        "1600x900": (By.XPATH, '//li[@data-size="1600x900"]'),
        "1920x1080": (By.XPATH, '//li[@data-size="1920x1080"]'),
        "2048x1152": (By.XPATH, '//li[@data-size="2048x1152"]'),
        "2400x1350": (By.XPATH, '//li[@data-size="2400x1350"]'),
        "2560x1440": (By.XPATH, '//li[@data-size="2560x1440"]'),
        "2880x1620": (By.XPATH, '//li[@data-size="2880x1620"]'),

        "2560x1080": (By.XPATH, '//li[@data-size="2560x1080"]'),
        "3440x1440": (By.XPATH, '//li[@data-size="3440x1440"]'),

        "3840x2160": (By.XPATH, '//li[@data-size="3840x2160"]'),
        "5120x2880": (By.XPATH, '//li[@data-size="5120x2880"]'),
        "7680x4320": (By.XPATH, '//li[@data-size="7680x4320"]'),

        "720x1280": (By.XPATH, '//li[@data-size="720x1280"]'),
        "1080x1920": (By.XPATH, '//li[@data-size="1080x1920"]'),
        "1080x2160": (By.XPATH, '//li[@data-size="1080x2160"]'),
        "1080x2400": (By.XPATH, '//li[@data-size="1080x2400"]'),
        "1440x2560": (By.XPATH, '//li[@data-size="1440x2560"]'),

        "750x1334": (By.XPATH, '//li[@data-size="750x1334"]'),
        "828x1792": (By.XPATH, '//li[@data-size="828x1792"]'),
        "1024x768": (By.XPATH, '//li[@data-size="1024x768"]'),
        "1024x1024": (By.XPATH, '//li[@data-size="1024x1024"]'),
        "1125x2436": (By.XPATH, '//li[@data-size="1125x2436"]'),
        "1170x2532": (By.XPATH, '//li[@data-size="1170x2532"]'),
        "1284x2778": (By.XPATH, '//li[@data-size="1284x2778"]'),
        "2048x1536": (By.XPATH, '//li[@data-size="2048x1536"]'),
        "2732x2048": (By.XPATH, '//li[@data-size="2732x2048"]')
    }


    RESOLUTION_IDS = (
        "Standard 4:3 1600x1200",
        "Standard 4:3 1920x1440",
        "Standard 4:3 2560x1920",
        "Standard 4:3 2800x2100",
        "Standard 4:3 3200x2400",

        "Standard 5:4 1280x1024",
        "Standard 5:4 2560x2048",

        "Wide 16:10 1152x720",
        "Wide 16:10 1280x800",
        "Wide 16:10 1440x900",
        "Wide 16:10 1680x1050",
        "Wide 16:10 1920x1200",
        "Wide 16:10 2560x1600",
        "Wide 16:10 2880x1800",

        "Wide 16:9 1024x576",
        "Wide 16:9 1280x720",
        "Wide 16:9 1366x768",
        "Wide 16:9 1600x900",
        "Wide 16:9 1920x1080",
        "Wide 16:9 2048x1152",
        "Wide 16:9 2400x1350",
        "Wide 16:9 2560x1440",
        "Wide 16:9 2880x1620",

        "UltraWide 21:9 2560x1080",
        "UltraWide 21:9 3440x1440",

        "UltraHD 3840x2160",
        "UltraHD 5120x2880",
        "UltraHD 7680x4320",

        "Android 720x1280",
        "Android 1080x1920",
        "Android 1080x2160",
        "Android 1080x2400",
        "Android 1440x2560",

        "IOS 750x1334",
        "IOS 828x1792",
        "IOS 1024x768",
        "IOS 1024x1024",
        "IOS 1125x2436",
        "IOS 1170x2532",
        "IOS 1284x2778",
        "IOS 2048x1536",
        "IOS 2732x2048"
    )

    #Top list
    TOP_LIST = {
        "Download": (By.XPATH, '//a[@href="https://wallscloud.net/ru/wallpapers/download"]'),
        "view": (By.XPATH, '//a[@href="https://wallscloud.net/ru/wallpapers/view"]'),
        "Favourite": (By.XPATH, '//a[@href="https://wallscloud.net/ru/wallpapers/favourite"]'),
        "Rating": (By.XPATH, '//a[@href="https://wallscloud.net/ru/wallpapers/rating"]')
    }

    #More List
    MORE_LIST = {
        "About-us": (By.XPATH, '//li[@id="more-list"]//a[@href="https://wallscloud.net/ru/about-us"]'),
        "Tags": (By.XPATH, '//li[@id="more-list"]//a[@href="https://wallscloud.net/ru/tags"]'),
        "Contact": (By.XPATH, '//li[@id="more-list"]//a[@href="https://wallscloud.net/ru/contact"]'),
        "Android_App": (By.XPATH, '//li[@id="more-list"]//li[@class="app_link"]/a')
    }

    #Color buttons
    COLORS = {
        "Aqua #00ffff": (By.CSS_SELECTOR, 'li.minicolors-swatch span[style*="rgb(0, 255, 255)"]'),
        "Black #000000": (By.CSS_SELECTOR, 'li.minicolors-swatch span[style*="rgb(0, 0, 0)"]'),
        "Blue #0000ff": (By.CSS_SELECTOR, 'li.minicolors-swatch span[style*="rgb(0, 0, 255)"]'),
        "Fuchsia #ff00ff": (By.CSS_SELECTOR, 'li.minicolors-swatch span[style*="rgb(255, 0, 255)"]'),
        "Gray #808080": (By.CSS_SELECTOR, 'li.minicolors-swatch span[style*="rgb(128, 128, 128)"]'),
        "Green #008000": (By.CSS_SELECTOR, 'li.minicolors-swatch span[style*="rgb(0, 128, 0)"]'),
        "Lime #00ff00": (By.CSS_SELECTOR, 'li.minicolors-swatch span[style*="rgb(0, 255, 0)"]'),
        "Maroon #800000": (By.CSS_SELECTOR, 'li.minicolors-swatch span[style*="rgb(128, 0, 0)"]'),
        "Navy #000080": (By.CSS_SELECTOR, 'li.minicolors-swatch span[style*="rgb(0, 0, 128)"]'),
        "Olive #808000": (By.CSS_SELECTOR, 'li.minicolors-swatch span[style*="rgb(128, 128, 0)"]'),
        "Purple #800080": (By.CSS_SELECTOR, 'li.minicolors-swatch span[style*="rgb(128, 0, 128)"]'),
        "Red #ff0000": (By.CSS_SELECTOR, 'li.minicolors-swatch span[style*="rgb(255, 0, 0)"]'),
        "Silver #c0c0c0": (By.CSS_SELECTOR, 'li.minicolors-swatch span[style*="rgb(192, 192, 192)"]'),
        "Teal #008080": (By.CSS_SELECTOR, 'li.minicolors-swatch span[style*="rgb(0, 128, 128)"]'),
        "White #ffffff": (By.CSS_SELECTOR, 'li.minicolors-swatch span[style*="rgb(255, 255, 255)"]'),
        "Yellow #ffff00": (By.CSS_SELECTOR, 'li.minicolors-swatch span[style*="rgb(255, 255, 0)"]'),
    }
    COLOR_VALUE = (By.XPATH, '//span[@class="value"]')

    LANGUAGE_SELECTORS = {
    "EN": (By.XPATH, '//a[@hreflang="en"]'),
    "RU": (By.XPATH, '//a[@hreflang="ru"]'),
    "UA": (By.XPATH, '//a[@hreflang="uk"]')
    }

    LOGIN_ITEMS = {
        "login" : (By.XPATH, '//a[@href="https://wallscloud.net/ru/account/login"]'),
        "signup" : (By.XPATH, '//a[@href="https://wallscloud.net/ru/account/signup"]')
    }