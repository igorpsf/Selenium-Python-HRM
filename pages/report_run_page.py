from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class ReportRunPage(BasePage):
    def __init__(self, driver):
        super(ReportRunPage, self).__init__(driver)
        self.page_url = "http://hrm-online.portnov.com/synfony/web/index.html"

    def get_report_header(self):
        return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR)))

