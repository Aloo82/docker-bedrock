import unittest, requests
    
from nose_parameterized import parameterized

class WordpressHardingTests(unittest.TestCase):
    
    @parameterized.expand([
        "https://www.mortgagestore.ie/wp/wp-login",
        "https://www.mortgagestore.ie/wp/wp-login/",
        "https://www.mortgagestore.ie/wp/wplogin/",
        "https://www.mortgagestore.ie/wp/wp-admin",
        "https://www.mortgagestore.ie/wp/wp-admin/",
        "https://www.mortgagestore.ie/wp/wp-admin.php",
        "https://www.mortgagestore.ie/wp/xmlrpc.php",
        "https://www.mortgagestore.ie/wp/wp-admin/install.php",
        "https://www.mortgagestore.ie/wp/wp-admin/about.php",
        "https://www.mortgagestore.ie/app/db.php",
        "https://www.mortgagestore.ie/app/wp-version.php",
        "https://www.mortgagestore.ie/wp/wp-login.php",
    ])
    ## Test: url returns 404
    def test_Returns404(self, url):
        ## Make the request
        r = requests.get(url)
        print("\nTest url: "+url+"\nExpected: 404 Result: "+str(r.status_code));
        self.assertEqual(r.status_code,404)
    
    @parameterized.expand([
        "https://www.mortgagestore.ie/wp/wp-admin/admin-ajax.php",
        "https://www.mortgagestore.ie/wp/wp-login.php?action=logout",
        "https://www.mortgagestore.ie/wp/wplogin?loggedout=true",
    ])
    ## Test: url returns 200
    def test_Returns404(self, url):
        ## Make the request
        r = requests.get(url)
        print("\nTest url: "+url+"\nExpected: 200 Result: "+str(r.status_code));
        self.assertEqual(r.status_code,200)
    
        