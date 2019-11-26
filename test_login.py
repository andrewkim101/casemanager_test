import os
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
        options.add_argument('--headless')
        #options.headless = True
				# paste the chromedriver in this location : C:\Program Files\Python37 (python installation folder)
       
        if platform.system() == 'Windows': 
            separ = '\\'
        else: 
            separ = '/'
        print(os.path.abspath(__file__) + separ + platform.system() + separ + 'chromedriver.exe')
        cls.driver = webdriver.Chrome(executable_path = platform.system() + '/chromedriver.exe', options=options)
        cls.driver.implicitly_wait(15)
        cls.driver.maximize_window()

        # open the page and enter the keyword
        cls.driver.get(cls.__website_path)


    def test_login(self):
        # """get the product name of listed products, search should be done before this function"""
        try:
            email_input = self.driver.find_element_by_id("session_email")
            email_input.send_keys("login")

            pass_input = self.driver.find_element_by_id("session_password")
            pass_input.send_keys("pass")

            btn_login = self.driver.find_element_by_xpath("/html/body/div/div/div/div/form/input[5]")
            btn_login.click()

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