from selenium import webdriver
import time
import unittest
import HtmlTestRunner

import sys
sys.path.append("/Users/sathu/PycharmProjects/OrangeHRMSite")


from SampleProjects.POMProjectDemo.Pages.loginpage import loginpage
from SampleProjects.POMProjectDemo.Pages.Homepage import Homepage


class loginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = loginpage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        time.sleep(3)
        login.click_login()
        time.sleep(2)

        homepage = Homepage(driver)
        homepage.click_welcome()
        time.sleep(2)
        homepage.click_logout()
        time.sleep(2)
        #self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        #self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        #self.driver.find_element_by_id("btnLogin").click()
        #time.sleep(3)
        #self.driver.find_element_by_xpath("//*[@id='welcome']").click()
        #time.sleep(3)
        #self.driver.find_element_by_link_text("Logout").click()
        #time.sleep(2)


    def test_02_login_Invalid_username(self):
        driver2 = self.driver
        driver2.get("https://opensource-demo.orangehrmlive.com/")

        login2 = loginpage(driver2)
        login2.enter_username("Admim1")
        login2.enter_password("admin2123")
        time.sleep(3)
        login2.click_login()
        time.sleep(2)
        message = driver2.find_element_by_xpath("").text
        self.assertEqual(message, "Invalid credentials123" )

        #self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        #self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        #self.driver.find_element_by_id("btnLogin").click()
        #time.sleep(3)
        #self.driver.find_element_by_xpath("//*[@id='welcome']").click()
        #time.sleep(3)
        #self.driver.find_element_by_link_text("Logout").click()
        #time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
        print("Git new")
        print("testing")
        print("closewindow")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/sathu/PycharmProjects/OrangeHRMSite/Reports'))