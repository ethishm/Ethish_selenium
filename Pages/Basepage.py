
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Basepage():

    def __init__(self,driver):

        self.driver = driver

    def do_click(self,by_locator):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(by_locator)).click()

    def do_sendkeys(self,by_locator,text):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_text(self,by_locator):

        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        return element.text()

    def get_title(self):

        return (self.driver.title)

    def Visibility_of_element(self,by_locator):

        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))

    def select_category_drp_down(self,option):

        element =  (By.XPATH,"//select[@name='categories']/option[text()='"+option+"']")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element)).click()

    def is_Element_visible(self,by_locator):

        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))

