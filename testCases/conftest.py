import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture
def setup(browser):
    if browser == 'chrome' or 'Chrome':
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        print("Launch chrome")
    elif browser == 'IE' or 'edge':
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        print("Launch Edge")
    driver.maximize_window()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


########################## html report generation ##############################

def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Sunil'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)
