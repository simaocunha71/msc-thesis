def ascii_value(char):
    return ord(char)

# test the function
print(ascii_value('A')) # output: 65
print(ascii_value('a')) # output: 97
print(ascii_value('0')) # output: 48
print(ascii_value(' ')) # output: 32

# Test case
assert ascii_value('A')==65
assert ascii_value('a')==97
assert ascii_value('0')==48
assert ascii_value(' ')==32

# Test case
import unittest
class TestAsciiValue(unittest.TestCase):
    def test_ascii_value(self):
        self.assertEqual(ascii_value('A'), 65)
        self.assertEqual(ascii_value('a'), 97)
        self.assertEqual(ascii_value('0'), 48)
        self.assertEqual(ascii_value(' '), 32)
if __name__ == '__main__':
    unittest.main()  # run the test case

# The function ascii_value() takes a character as an argument and returns its ASCII value.
# The built-in Python function ord() is used to convert a character to its ASCII value. This function is used in the ascii_value() function. 
# The unit test case is used to verify the function's correctness. It checks the ASCII values of 'A', 'a', '0', and ' '. 
# The test case ensures that the function works correctly for different types of characters. 
# The test case is run using the unittest module.  # run the test case

# The function ascii_value() takes a character as an argument and returns its ASCII value.
# The built-in Python function ord() is used to convert a character to its ASCII value. This function is used in the ascii_value() function. 
# The unit test case is used to verify the function's correctness. It checks the ASCII values of 'A', 'a', '0', and ' '. 
# The test case ensures that the function works correctly for different types of characters. 
# The test case is run using the unittest module.  # run the test case
# The function ascii_value() takes a character as an argument and returns its ASCII value.
# The built-in Python function ord() is used to convert a character to its ASCII value. This function is used in the ascii_value() function. 
# The unit test case is used to verify the function's correctness. It checks the ASCII values of 'A', 'a', '0', and ' '. 
# The test case ensures that