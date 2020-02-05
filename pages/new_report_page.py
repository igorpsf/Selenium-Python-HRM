from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NewReportPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 2)

    def set_name(self, report_name):
        self.wait.until(EC.presence_of_element_located((By.ID, "report_report_name"))).send_keys(report_name)

    def setelect_selection_criteria(self, param):
        pass

    def select_display_field_groups(self, param):
        pass

    def enable_display_fields(self):
        pass

    def save(self):
        pass

