import os

class Testdata:

    Base_url = "https://letskodeit.com/"
    DIR = os.getcwd()
    Username = "test@email.com"
    Password = "abcabc"

    CHROME_EXECUTABLE_PATH = r"{}\Drivers\chromedriver.exe".format(DIR)
    FIREFOX_EXECUTABLE_PATH = r"{}\Drivers\geckodriver.exe".format(DIR)