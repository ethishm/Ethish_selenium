from Pages.Basepage import Basepage
from Config.config import Testdata

from selenium.webdriver.common.by import By

class LoginPage(Basepage):


     sign_in_btn_label = (By.XPATH,"//*[contains(text(), 'Sign Up or Log In')]")
     login_in_btn_label = (By.XPATH,"//*[contains(@value, 'Login')]")
     username_input_field = (By.ID,"email")
     password_input_field = (By.ID,"password")
     Mycourse_header = (By.XPATH,"//*[contains(@class, 'dynamic-heading') and text() = 'My Courses ']")
     course_selenium_java = (By.XPATH,"//*[contains(text(), 'Selenium WebDriver With Java') and @class = 'dynamic-heading']")
     all_courses_tab_label =(By.XPATH,"//*[contains(@href,'/courses') and text() = 'ALL COURSES']")

     category_label = (By.XPATH,"//*[contains(@class, 'dynamic-text') and text() = 'Category']")

     category_drp_down = (By.NAME,"categories")

     def __init__(self,driver):

         super().__init__(driver)
         self.driver.delete_all_cookies()
         self.driver.get(Testdata.Base_url)
         title = self.get_title()
         assert title == "Let's Kode It – Anyone Can Code"

     def click_sign_in(self):

         self.do_click(self.sign_in_btn_label)


     def login(self,username,password):

         self.click_sign_in()
         self.do_sendkeys(self.username_input_field,username)
         self.do_sendkeys(self.password_input_field,password)
         self.do_click(self.login_in_btn_label)



     def validate_homepage_headings(self):

         self.Visibility_of_element(self.Mycourse_header)

     def go_to_All_courses_tab(self):

         self.do_click(self.all_courses_tab_label)
         self.Visibility_of_element(self.category_label)

     def  search_testing_course(self):

         self.do_click(self.category_drp_down)
         self.select_category_drp_down("Sofware Testing")

