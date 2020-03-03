from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class ReportRunPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.page_url = "http://hrm-online.portnov.com/synfony/web/index.html"
        self.wait = WebDriverWait(self.driver, 2)

    def get_report_header(self):
        return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR)))

