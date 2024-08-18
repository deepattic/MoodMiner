import unittest
from app import *

# yelp review im testing for now
comment: str = "Same great ice cream flavor and friendly service as in the S 18th street location. This location is not as small but it's hard to talk to friends. Thankfully there is great outdoor seating to escape the noise."

class MyFirstTests(unittest.TestCase):
# Basic filtering
   def test_basic_filter(self):
      given: str = comment
      expected: str = "same great ice cream flavor and friendly service as in the s 18th street location this location is not as small but its hard to talk to friends thankfully there is great outdoor seating to escape the noise"
      self.assertEqual(basic_filter(given), expected)

   def test_tokenization(self):
      given: str = basic_filter(comment)
      expected: list[str] = ["same", "great", "ice", "cream", "flavor", "and", "friendly", "service", "as", "in", "the", "s", "18th", "street", "location", "this", "location", "is", "not", "as", "small", "but", "its", "hard", "to", "talk", "to", "friends", "thankfully", "there", "is", "great", "outdoor", "seating", "to", "escape", "the", "noise"]
      self.assertEqual(tokenize(given), expected)

   def test_stop_word_filter(self):
      given: list[str] = ["same", "great", "ice", "cream", "flavor", "and", "friendly", "service", "as", "in", "the", "s", "18th", "street", "location", "this", "location", "is", "not", "as", "small", "but", "its", "hard", "to", "talk", "to", "friends", "thankfully", "there", "is", "great", "outdoor", "seating", "to", "escape", "the", "noise"]
      expected: list[str] = ["same", "great", "ice", "cream", "flavor", "friendly", "service", "s", "18th", "street", "location", "this", "location", "not", "as", "small", "but", "hard", "talk", "to", "friends", "thankfully", "there", "is", "great", "outdoor", "seating", "to", "escape", "the", "noise"]
      self.assertEqual(stop_word_filter(given), expected)


if __name__ == "__main__":
   unittest.main()
