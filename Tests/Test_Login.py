
from Tests.test_base import Test_base
from Pages.loginpage import LoginPage
from Config.config import Testdata

class Test_login(Test_base):

    def test_login(self):

        self.loginpy = LoginPage(self.driver)
        self.loginpy.login(Testdata.Username,Testdata.Password)

    def test_validate_home_page(self):
        self.loginpy = LoginPage(self.driver)
        self.loginpy.login(Testdata.Username, Testdata.Password)
        self.loginpy.validate_homepage_headings()

    def test_navigate_all_courses_tab(self):

        self.loginpy = LoginPage(self.driver)
        self.loginpy.login(Testdata.Username, Testdata.Password)
        self.loginpy.go_to_All_courses_tab()

    def test_find_course_for_testing(self):

        self.loginpy = LoginPage(self.driver)
        self.loginpy.login(Testdata.Username, Testdata.Password)
        self.loginpy.go_to_All_courses_tab()
        self.loginpy.search_testing_course()
        self.loginpy.is_Element_visible(self.loginpy.course_selenium_java)



