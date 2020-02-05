class ReportsPage:
    def __init__(self, driver):
        self.driver = driver

    def add(self):
        driver = self.driver
        driver.find_element_by_id("btnAdd").click()

    def search(self, report_name):
        pass

    def run(self, report_name):
        pass

    