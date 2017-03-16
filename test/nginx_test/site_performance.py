import unittest, requests
    
from nose_parameterized import parameterized

class SitePerformanceTests(unittest.TestCase):
    
    @parameterized.expand([
        ("https://www.mortgagestore.ie/", 0.6),
        ("https://www.mortgagestore.ie/404/", 0.6),
        ("https://www.mortgagestore.ie/mortgage-calculator/", 0.6),
        ("https://www.mortgagestore.ie/50x.html", 0.1),
    ])
    ## Test: page response time
    def test_PageResponseTime(self, url, maxTime):
        ## Make the request
        r = requests.get(url)
        t = r.elapsed.total_seconds()
        print("\nTest url: "+url+"\nExpected: < "+str(maxTime)+"s Result: "+str(t));
        self.assertTrue((t < maxTime))
        