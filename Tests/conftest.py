

import pytest
from selenium import webdriver
from Config.config import Testdata


@pytest.fixture(params=["chrome"],scope='class')
def init_driver(request):

    if request.param == "chrome":

        web_driver = webdriver.Chrome(executable_path=Testdata.CHROME_EXECUTABLE_PATH)

    if request.param == "firefox":

        web_driver = webdriver.Firefox(executable_path=Testdata.FIREFOX_EXECUTABLE_PATH)

    request.cls.driver = web_driver
    yield
    web_driver.close()




