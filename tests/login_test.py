import unittest

from selenium import webdriver
from time import sleep

from steps.common import login, get_welcome_message, logout


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/igor/Desktop/Docs/Git/Python/Selenium-Python-HRM/chromedriver/chromedriver")
        self.driver.get("http://hrm-online.portnov.com/")

    def tearDown(self):
        self.driver.quit()

    def test_valid_login(self):
        driver = self.driver

        login(driver)

        welcome_text = get_welcome_message(driver)

        # Expected value vs. Actual value
        self.assertEqual("Welcome Admin", welcome_text)

        logout(driver)

    def test_invalid_password(self):
        driver = self.driver
        driver.find_element_by_id("txtUsername").send_keys("Admin")
        driver.find_element_by_id("txtPassword").send_keys("Admin123")
        driver.find_element_by_id("btnLogin").click()

        warning_text = driver.find_element_by_id("spanMessage").text

        # Expected value vs. Actual value
        self.assertEqual("Invalid credentials", warning_text)

    def test_empty_password(self):
        driver = self.driver
        driver.find_element_by_id("txtUsername").send_keys("Admin")
        driver.find_element_by_id("txtPassword").send_keys("")
        driver.find_element_by_id("btnLogin").click()

        warning_text = driver.find_element_by_id("spanMessage").text

        # Expected value vs. Actual value
        self.assertEqual("Password cannot be empty", warning_text)


if __name__ == '__main__':
    unittest.main()
