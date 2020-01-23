from random import randint
import unittest
from time import sleep

from selenium import webdriver


class AddEmployee(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/igor/Desktop/Docs/Git/Python/Selenium-Python-HRM/chromedriver/chromedriver")
        self.driver.get("http://hrm-online.portnov.com/")

    def tearDown(self):
        self.driver.quit()

    def test_something(self):
        # Login

        empId = randint(100000, 999999)
        driver = self.driver
        driver.find_element_by_id("txtUsername").send_keys("admin")
        driver.find_element_by_id("txtPassword").send_keys("password")
        driver.find_element_by_id("btnLogin").click()

        sleep(2)

        welcome_text = driver.find_element_by_id("welcome").text

        # Expected value vs. Actual value
        self.assertEqual("Welcome Admin", welcome_text)

        # Click the Add button
        driver.find_element_by_id("btnAdd").click()
        # TODO IP: may need to come back and do "something"

        # Enter First and Last name
        driver.find_element_by_id("firstName").send_keys("Elon")
        driver.find_element_by_id("lastName").send_keys("Musk")

        # Enter and remember the EmpId
        driver.find_element_by_id("employeeId").clear()
        driver.find_element_by_id("employeeId").send_keys(empId)

        # Save the Employee
        driver.find_element_by_id("btnSave").click()

        # Go to PIM page
        driver.find_element_by_id("menu_pim_viewPimModule").click()
        # TODO IP: may need to come back and do "something"

        # Search by EmpId
        driver.find_element_by_id("empsearch_id").send_keys(empId)
        driver.find_element_by_id("searchBtn").click()

        # Expected: 1 record back
        lst = driver.find_elements_by_xpath("//td[3]/a")
        print(len(lst))
        self.assertTrue(len(lst) == 1)

        # Expected Correct Name and EmpId
        firstName = driver.find_element_by_xpath("//td[3]/a").text
        lastName = driver.find_element_by_xpath("//td[4]/a").text

        self.assertEqual("Elon", firstName)
        self.assertEqual("Musk", lastName)


if __name__ == '__main__':
    unittest.main()
