"""
def text_match_wordz_middle(text):
    if 'z' in text:
        if (text[0] == 'z' or text[-1] == 'z'):
            return False
        else:
            return True
    else:
        return False
"""

# This code is dangerous! It will cause a `IndexError` when `text` is an empty string or a single character.
# Here's a safer version that checks if the first and last character of the string are 'z':

def text_match_wordz_middle(text):
    if 'z' in text:
        return text[0] != 'z' and text[-1] != 'z'
    else:
        return False

# To test the function, you can use the `unittest` module:

import unittest

class TestTextMatchWordzMiddle(unittest.TestCase):
    def test_text_match_wordz_middle(self):
        self.assertEqual(text_match_wordz_middle("pythonzabc."), True)
        self.assertEqual(text_match_wordz_middle("z"), False)
        self.assertEqual(text_match_wordz_middle(""), False)
        self.assertEqual(text_match_wordz_middle("z."), False)

if __name__ == "__main__":
    unittest.main()

# The `unittest` module provides a framework for writing and running unit tests in Python. It allows you to define test cases and assertions, and run them to verify the correctness of your functions.

# In the code above, we define a test case class `TestTextMatchWordzMiddle` that inherits from `unittest.TestCase`. Inside this class, we define a test method `test_text_match_wordz_middle` that contains assertions to verify the correctness of the `text_match_wordz_middle` function.

# To run the tests, we use the `unittest.main()` function, which discovers and runs all test methods in the current module. This will print the result of each test case to the console, indicating whether the test passed or failed.

"""

# This code defines a function `text_match_