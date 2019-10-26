import unittest
import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class LoginTest(unittest.TestCase):
	 # test data
    __website_path = "https://desolate-beach-90661.herokuapp.com/"

    @classmethod
    def setUpClass(cls):
        """initialize the browser and opens the page"""
        #platform.system()
        options = Options()
        options.headless = True
				# paste the chromedriver in this location : C:\Program Files\Python37 (python installation folder)
        cls.driver = webdriver.Chrome('./'+platform.system() + '/chromedriver.exe',options=options)
        cls.driver.implicitly_wait(15)
        cls.driver.maximize_window()

        # open the page and enter the keyword
        cls.driver.get(cls.__website_path)


    def test_login(self):
        # """get the product name of listed products, search should be done before this function"""
        try:
            email_input = self.driver.find_element_by_id("session_email")
            email_input.keys("imelist@houseofkim.info")
            # assert number of products
            #self.assertEqual(7, len(product_name_list))

            # assert product names
            #for element in product_name_list:
            #    self.assertTrue(word.lower() in element.text.lower())
        
        except AssertionError as error:
            print(f"Handled Assertation: {error}")
        except Exception as other:
            print(f"Other exceptions occured : {other}")
            
    @classmethod
    def tearDownClass(cls):
        # close the browser
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)