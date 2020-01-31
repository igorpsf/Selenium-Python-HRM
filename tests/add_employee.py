from random import randint
import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from steps.common import login, get_welcome_message, logout


class AddEmployee(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/igor/Desktop/Docs/Git/Python/Selenium-Python-HRM/chromedriver/chromedriver")
        self.driver.get("http://hrm-online.portnov.com/")
        self.wait = WebDriverWait(self.driver, 25)

    def tearDown(self):
        self.driver.quit()

    def test_something(self):

        empId = randint(100000, 999999)
        expected_job_title = "CEO"
        expected_employment_status = "Full Time"
        expected_first_name = "Elon"
        expected_last_name = "Musk"
        username = "jb" + str(empId)

        driver = self.driver

        login(driver)

        welcome_text = get_welcome_message(driver)

        # Expected value vs. Actual value
        self.assertEqual("Welcome Admin", welcome_text)

        # Click the Add button
        #self.wait.until(expected_conditions.visibility_of_element_located((By.ID, "btnAdd"))).click()
        #driver.find_element_by_id("btnAdd").click()
        WebDriverWait(driver, 2).until(
            expected_conditions.presence_of_element_located((By.ID, "btnAdd"))).click()

        # Enter First and Last name
        self.wait.until(expected_conditions.visibility_of_element_located((By.ID, "firstName"))).send_keys(expected_first_name)
        #driver.find_element_by_id("firstName").send_keys(expected_first_name)
        driver.find_element_by_id("lastName").send_keys(expected_last_name)

        # Enter and remember the EmpId
        driver.find_element_by_id("employeeId").clear()
        driver.find_element_by_id("employeeId").send_keys(empId)

        # Click Create Login Details checkbox
        driver.find_element_by_id("chkLogin").click()

        # Wait for the fields to be available
        # Fill them in
        self.wait.until(expected_conditions.visibility_of_element_located((By.ID, "user_name"))).send_keys(username)
        driver.find_element_by_id("user_password").send_keys("password")
        driver.find_element_by_id("re_password").send_keys("password")

        # Save the Employee
        driver.find_element_by_id("btnSave").click()

        driver.find_element_by_link_text("Job").click()
        driver.find_element_by_id("btnSave").click()

        Select(driver.find_element_by_id("job_job_title")).select_by_visible_text(expected_job_title)
        Select(driver.find_element_by_id("job_emp_status")).select_by_visible_text(expected_employment_status)

        driver.find_element_by_id("btnSave").click()
        locator = (By.CSS_SELECTOR, ".message.success")
        self.wait.until(expected_conditions.presence_of_element_located(locator))

        # Go to PIM page
        driver.find_element_by_id("menu_pim_viewPimModule").click()
        # TODO IP: may need to come back and do "something"

        # Search by EmpId
        driver.find_element_by_id("empsearch_id").send_keys(empId)
        driver.find_element_by_id("searchBtn").click()

        # Expected: 1 record back
        #locator2 = (By.XPATH, "//td[3]/a")
        #self.wait.until(expected_conditions.visibility_of_element_located(locator2))
        #lst = len(driver.find_elements_by_xpath("//td[3]/a"))
        #self.assertTrue(lst == 1)

        # Expected Correct Name and EmpId
        firstName = driver.find_element_by_xpath("//td[3]/a").text
        lastName = driver.find_element_by_xpath("//td[4]/a").text
        job_title = driver.find_element_by_xpath("//td[5]").text
        employment_status = driver.find_element_by_xpath("//td[6]").text

        message = "Expected the table to contains first name '{0}' but instead the value was '{1}'"
        self.assertEqual(expected_first_name, firstName, message.format(expected_first_name, firstName))
        self.assertEqual(expected_last_name, lastName, message.format(expected_last_name, lastName))
        self.assertEqual(expected_job_title, job_title, message.format(expected_job_title, job_title))
        self.assertEqual(employment_status, employment_status, message.format(employment_status, employment_status))

        # Logout
        logout()

        # Login
        login(driver, username)

        # Check welcome message
        self.assertEqual("Welcome " + expected_first_name , get_welcome_message(driver))

        # Logout
        logout(driver)

if __name__ == '__main__':
    unittest.main()
