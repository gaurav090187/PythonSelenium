import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
import allure

driver = None


@pytest.fixture(scope='class')
def setup_teardown(request, browser):
    global driver
    if browser == 'chrome':
        chrome_option = webdriver.ChromeOptions()
        chrome_service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=chrome_service, options=chrome_option)
    elif browser == 'firefox':
        firefox_option = webdriver.FirefoxOptions()
        firefox_service = Service(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(options=firefox_option, service=firefox_service)
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get('https://rahulshettyacademy.com/angularpractice/')
    request.cls.driver = driver
    yield
    driver.quit()


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')


@pytest.fixture(scope='class')
def browser(request):
    return request.config.getoption('--browser')


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup_teardown":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    # driver.get_screenshot_as_file(name)
    allure.attach(driver.get_screenshot_as_png(),
                  name=name,
                  attachment_type=allure.attachment_type.PNG)
