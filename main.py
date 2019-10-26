import unittest
from .test_login import LoginTest
#from .test_ime import SearchTests

# save classes as tests
#search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTests)
#homepage_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTests)
log_in_test = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
# create a suite from loaded TestCases
test_list =[log_in_test]
regression = unittest.TestSuite(test_list)

# execute the test
unittest.TextTestRunner(verbosity=2).run(regression)