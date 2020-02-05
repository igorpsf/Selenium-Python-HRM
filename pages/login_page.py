class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username="admin", password="password"):
        driver = self.driver
        driver.find_element_by_id("txtUsername").send_keys(username)
        driver.find_element_by_id("txtPassword").send_keys(password)
        driver.find_element_by_id("btnLogin").click()

    def get_warning_message(self):
        return self.driver.find_element_by_id("spanMessage").text