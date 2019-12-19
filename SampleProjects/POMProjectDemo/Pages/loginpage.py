from SampleProjects.POMProjectDemo.Locators.locators import Locators

class loginpage():

    def __init__(self, driver): #constructor
        self.driver=driver

        # 3 object
        self.username_textbox_id = Locators.username_textbox_id
        self.password_textbox_id= Locators.password_textbox_id
        self.login_button=Locators.login_button
        self.InvalidUsername_message_xpath="//span[@id='spanMessage']"

    #function or action method

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys("Admin")

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys("admin123")

    def click_login(self):
        self.driver.find_element_by_id(self.login_button).click()

    def check_invalid_username_message(self):
        msg = self.driver.find_element_by_xpath(self.InvalidUsername_message_xpath).text
        return msg