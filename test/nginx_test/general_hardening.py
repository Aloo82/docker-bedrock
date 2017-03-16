import unittest, requests
    
from nose_parameterized import parameterized

class GeneralHardingTests(unittest.TestCase):
    
    @parameterized.expand([
        "https://www.mortgagestore.ie/404",
        "https://www.mortgagestore.ie/wp/readme.html",
        "https://www.mortgagestore.ie/wp/license.txt",
        "https://www.mortgagestore.ie/wp/composer.json",
        "https://www.mortgagestore.ie/app/plugins/wp-utilities/README.md",
        "https://www.mortgagestore.ie/app/plugins/wp-utilities/settings.json",
        "https://www.mortgagestore.ie/app/plugins/wp-utilities/config.ini",
        "https://www.mortgagestore.ie/app/plugins/wp-utilities/.gitignore",
    ])
    ## Test: url returns 404
    def test_Returns404(self, url):
        ## Make the request
        r = requests.get(url)
        print("\nTest url: "+url+"\nExpected: 404 Result: "+str(r.status_code));
        self.assertEqual(r.status_code,404)
    
    @parameterized.expand([
        ("https://www.mortgagestore.ie/","TRACE"),
        ("https://www.mortgagestore.ie/","TRACK"),
        ("https://www.mortgagestore.ie/","DELETE"),
    ])
    ## Test: banned request types return 403
    def test_Returns403(self, url, method):
        ## Make the request
        r = requests.request(method, url)
        print("\nTest url: "+url+" method: "+method+" \nExpected: 403 Result: "+str(r.status_code));
        self.assertEqual(r.status_code,403)
    
    @parameterized.expand([
        "https://www.mortgagestore.ie/",
    ])
    ## Test: ../ is stripped from params
    def test_DirectoryTraversalParamValues(self, url):
        ## Make the request
        r = requests.get(url + "?directory=../")
        found = ("../" in r.url)
        print("\nTest url: "+url+"?directory=../ \nExpected: Not found Result: "+("Found" if found else "Not found"));
        self.assertFalse(found)
        