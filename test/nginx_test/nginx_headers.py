import unittest, requests
    
from nose_parameterized import parameterized

class HeaderTests(unittest.TestCase):
    
    @parameterized.expand([
        ## X-Frame-Options
        ("https://www.mortgagestore.ie/", "X-Frame-Options", "SAMEORIGIN"),
        ("https://www.mortgagestore.ie/articles-list/", "X-Frame-Options", "SAMEORIGIN"),
        ("https://www.mortgagestore.ie/category/first-time-buyers/", "X-Frame-Options", "SAMEORIGIN"),
        ("https://www.mortgagestore.ie/category/moving-home/", "X-Frame-Options", "SAMEORIGIN"),
        ("https://www.mortgagestore.ie/404", "X-Frame-Options", "SAMEORIGIN"),
        ("https://www.mortgagestore.ie/50x.html", "X-Frame-Options", "SAMEORIGIN"),
        ## X-Content-Type-Options
        ("https://www.mortgagestore.ie/", "X-Content-Type-Options", "nosniff"),
        ("https://www.mortgagestore.ie/articles-list/", "X-Content-Type-Options", "nosniff"),
        ("https://www.mortgagestore.ie/category/first-time-buyers/", "X-Content-Type-Options", "nosniff"),
        ("https://www.mortgagestore.ie/category/moving-home/", "X-Content-Type-Options", "nosniff"),
        ("https://www.mortgagestore.ie/404", "X-Content-Type-Options", "nosniff"),
        ("https://www.mortgagestore.ie/50x.html", "X-Content-Type-Options", "nosniff"),
        ## X-XSS-Protection
        ("https://www.mortgagestore.ie/", "X-XSS-Protection", "1; mode=block"),
        ("https://www.mortgagestore.ie/articles-list/", "X-XSS-Protection", "1; mode=block"),
        ("https://www.mortgagestore.ie/category/first-time-buyers/", "X-XSS-Protection", "1; mode=block"),
        ("https://www.mortgagestore.ie/category/moving-home/", "X-XSS-Protection", "1; mode=block"),
        ("https://www.mortgagestore.ie/404", "X-XSS-Protection", "1; mode=block"),
        ("https://www.mortgagestore.ie/50x.html", "X-XSS-Protection", "1; mode=block"),
        ## Strict-Transport-Security
        ("https://www.mortgagestore.ie/", "Strict-Transport-Security", "max-age=31536000; includeSubdomains; preload"),
        ("https://www.mortgagestore.ie/articles-list/", "Strict-Transport-Security", "max-age=31536000; includeSubdomains; preload"),
        ("https://www.mortgagestore.ie/category/first-time-buyers/", "Strict-Transport-Security", "max-age=31536000; includeSubdomains; preload"),
        ("https://www.mortgagestore.ie/category/moving-home/", "Strict-Transport-Security", "max-age=31536000; includeSubdomains; preload"),
        ("https://www.mortgagestore.ie/404", "Strict-Transport-Security", "max-age=31536000; includeSubdomains; preload"),
        ("https://www.mortgagestore.ie/50x.html", "Strict-Transport-Security", "max-age=31536000; includeSubdomains; preload"),
        ## Cache-Control
        ("https://www.mortgagestore.ie/", "Cache-Control", "no-cache, no-store, must-revalidate, private"),
        ("https://www.mortgagestore.ie/articles-list/", "Cache-Control", "no-cache, no-store, must-revalidate, private"),
        ("https://www.mortgagestore.ie/category/first-time-buyers/", "Cache-Control", "no-cache, no-store, must-revalidate, private"),
        ("https://www.mortgagestore.ie/category/moving-home/", "Cache-Control", "no-cache, no-store, must-revalidate, private"),
        #("https://www.mortgagestore.ie/404", "Cache-Control", "no-cache, no-store, must-revalidate, private"),
        ("https://www.mortgagestore.ie/50x.html", "Cache-Control", "no-cache, no-store, must-revalidate, private"),
    ])
    ## Test if requested URL response header is equal to value
    def test_HeaderOptionEquals(self, url, header, expect):
        ## Make the request
        r = requests.get(url)
        print("\nTest header: "+header+" url: "+url+"\nExpected: "+expect+" Found: "+r.headers.get(header));
        self.assertEqual(r.headers.get(header),expect)
        
        
    @parameterized.expand([
        ## Cache-Control
        ("https://www.mortgagestore.ie/", "Cache-Control", "no-cache"),
        ("https://www.mortgagestore.ie/articles-list/", "Cache-Control", "no-cache"),
        ("https://www.mortgagestore.ie/category/first-time-buyers/", "Cache-Control", "no-cache"),
        ("https://www.mortgagestore.ie/category/moving-home/", "Cache-Control", "no-cache"),
        ("https://www.mortgagestore.ie/404", "Cache-Control", "no-cache"),
        ("https://www.mortgagestore.ie/50x.html", "Cache-Control", "no-cache")
    ])
    ## Test if requested URL response header contains value
    def test_HeaderOptionEquals(self, url, header, contains):
        ## Make the request
        r = requests.get(url)
        found = (contains in r.headers.get(header))
        print("\nTest header: "+header+" url: "+url+"\nContains: "+contains+" Found: "+("True" if found else "False"));
        self.assertTrue(found)

    