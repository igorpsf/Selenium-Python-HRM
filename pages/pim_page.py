class PIMPage:
    def __init__(self, driver):
        self.driver = driver

    def goto_reports(self):
        driver = self.driver
        driver.find_element_by_id("menu_pim_viewPimModule").click()
        driver.find_element_by_id("menu_core_viewDefinedPredefinedReports").click()

