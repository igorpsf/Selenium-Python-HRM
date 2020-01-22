import unittest

from selenium import webdriver
from time import sleep

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/igor/Desktop/Docs/Git/Python/Selenium-Python-HRM/chromedriver/chromedriver")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")


    def test_valid_login(self):
        driver = self.driver
        driver.find_element_by_id("txtUsername").send_keys("Admin")
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()

        sleep(2)

        welcome_text = driver.find_element_by_id("welcome").text

        # Expected value vs. Actual value
        self.assertEqual("Welcome Admin", welcome_text)


if __name__ == '__main__':
    unittest.main()
