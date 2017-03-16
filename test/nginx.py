import unittest, requests

if __name__ == "__main__":
    all_tests = unittest.TestLoader().discover('nginx_test', pattern='*.py')
    unittest.TextTestRunner().run(all_tests)