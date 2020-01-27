import unittest

from selenium import webdriver


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/igor/Desktop/Docs/Git/Python/Selenium-Python-HRM/chromedriver/chromedriver")
        self.driver.get("http://hrm-online.portnov.com/")

    def tearDown(self):
        self.driver.quit()

    def test_logo_size_and_location(self):
        driver = self.driver

        # Login
        driver.find_element_by_id("txtUsername").send_keys("admin")
        driver.find_element_by_id("txtPassword").send_keys("password")
        driver.find_element_by_id("btnLogin").click()

        logo_element = driver.find_element_by_xpath("//*[@id='branding']/img")
        #css - driver.find_element_by_css_selector("#branding > img")

        logo_size = logo_element.size

        # Expected and Actual
        self.assertEqual(56, logo_size.get("height"))
        self.assertTrue(logo_size.get("width") == 283)
        self.assertDictEqual({'width': 283, 'height': 56}, logo_size)

        window_size = driver.get_window_size()

        logo_location = logo_element.location

        top_right_logo_corner_x_location = logo_size.get('width') + logo_location.get('x')

        # The entire logo (width) fits within the left half of the window
        self.assertTrue(top_right_logo_corner_x_location < (window_size.get('width') / 2))


if __name__ == '__main__':
    unittest.main()
