import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options


#  Функция pytest'а, позволяющая запускать тесты с определёнными параметрами
def pytest_addoption(parser):
    #  Добавление выбора языка браузера при запуске тестовp
    parser.addoption('--language', action='store', default='en',
                     help="Choose language:ru, eng, fr, gb...")
    #  Добавление выбора браузера при запуске тестов
    parser.addoption('--browser', action='store', default='chrome',
                     help="Choose browser:chrome or firefox")


#  Фикстура запуска браузера
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser')
    user_language = request.config.getoption('language')
    browser = None

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        #  Создаём класс настроек
        options = Options()
        #  Добавляем в настройки установку языка на выбранный
        options.add_experimental_option('prefs', {"intl.accept_languages": user_language})
        #  Запускаем браузер с созданными настройками
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        #  Добавление Гекодрайвера в патч через питон
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=fp)
    else:
        #  Выброс ошибки при неуказании или указании неверного параметра выбора браузера
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()
