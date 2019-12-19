from SampleProjects.POMProjectDemo.Locators.locators import Locators

class Homepage():

    def __init__(self,driver):
        self.driver=driver

        self.welcome_link_xpath=Locators.welcome_link_xpath
        self.logout_link_text=Locators.logout_link_text

    def click_welcome(self):
        self.driver.find_element_by_xpath(self.welcome_link_xpath).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_link_text).click()


