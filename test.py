import unittest
from app import *

# yelp review im testing for now
comment: str = "Same great ice cream flavor and friendly service as in the S 18th street location. This location is not as small but it's hard to talk to friends. Thankfully there is great outdoor seating to escape the noise."

class MyFirstTests(unittest.TestCase):
# Basic filtering
   def test_basic_filter(self):
      given: str = comment
      expected: str = "Same great ice cream flavor and friendly service as in the S 18th street location This location is not as small but its hard to talk to friends Thankfully there is great outdoor seating to escape the noise"
      self.assertEqual(basic_filter(given), expected)

if __name__ == "__main__":
   unittest.main()
