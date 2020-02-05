import random
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from steps.common import login


class ReportTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            "/Users/igor/Desktop/Docs/Git/Python/Selenium-Python-HRM/chromedriver/chromedriver")
        self.driver.get("http://hrm-online.portnov.com/")
        self.wait = WebDriverWait(self.driver, 2)

    def tearDown(self):
        driver = self.driver
        if self.report_name:
            driver.find_element_by_id("menu_pim_viewPimModule").click()
            driver.find_element_by_id("menu_core_viewDefinedPredefinedReports").click()

            driver.find_element_by_id("search_search").send_keys(self.report_name)
            driver.find_element_by_class_name("searchBtn").click()

            driver.find_element_by_css_selector("td>input").click()
            driver.find_element_by_id("btnDelete").click()

            self.wait.until(EC.visibility_of_element_located((By.ID, "dialogDeleteBtn"))).click()

        # tearDown: remove the report

        self.driver.quit()

    def test_create_report(self):
        report_name = "IP Report #" + str(random.randint(1, 100))
        self.report_name = report_name

        driver = self.driver
        login(driver)

        # Click on the report tab
        driver.find_element_by_id("menu_pim_viewPimModule").click()
        driver.find_element_by_id("menu_core_viewDefinedPredefinedReports").click()

        # Click on the Add button
        # Enter unique Report Name
        driver.find_element_by_id("btnAdd").click()
        self.wait.until(EC.presence_of_element_located((By.ID, "report_report_name"))).send_keys(report_name)

        # Select Criteria = Job Title
        Select(driver.find_element_by_id("report_criteria_list")).select_by_visible_text("Job Title")
        driver.find_element_by_id("btnAddConstraint").click()

        # Select Display Field Group = Personal
        Select(driver.find_element_by_id("report_display_groups")).select_by_visible_text("Personal")
        driver.find_element_by_id("btnAddDisplayGroup").click()

        # make sure to check the checkbox and Save
        driver.find_element_by_id("display_group_1").click()
        driver.find_element_by_id("btnSave").click()

        # verify the report was created
        a = self.assertTrue(self.is_element_present(By.XPATH, "//td[text()='{0}']".format(report_name)))
        print(a)

        # Run the report
        driver.find_element_by_xpath("//td[text()='{0}}']/../td[3]/a".format(report_name)).click()

        # verify the report works
        report_header = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".head h1"))).text
        self.assertEqual("Report Name : {0}".format(report_name), report_header)


if __name__ == "__main__":
    unittest.main()