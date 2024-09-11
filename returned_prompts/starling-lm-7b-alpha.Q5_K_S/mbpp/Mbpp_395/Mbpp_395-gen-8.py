def first_non_repeating_character(string):
    char_count = {}
    for char in string:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    for char in string:
        if char_count[char] == 1:
            return char
    return None

# Test
print(first_non_repeating_character("abcabc")) # None
print(first_non_repeating_character("abcabcdd")) # 'd'
print(first_non_repeating_character("abcabcdde")) # 'e'
print(first_non_repeating_character("abcabcddeff")) # 'f'
print(first_non_repeating_character("aaabbb")) # None

# Run tests
import unittest

class TestStringMethods(unittest.TestCase):
    def test_first_non_repeating_character(self):
        self.assertEqual(first_non_repeating_character("abcabc"), None)
        self.assertEqual(first_non_repeating_character("abcabcdd"), 'd')
        self.assertEqual(first_non_repeating_character("abcabcdde"), 'e')
        self.assertEqual(first_non_repeating_character("abcabcddeff"), 'f')
        self.assertEqual(first_non_repeating_character("aaabbb"), None)

if __name__ == '__main__':
    unittest.main()


"""
In this solution, we first create a dictionary to keep track of the count of each character in the string. Then, we iterate through the string again and return the first character that has a count of 1 in the dictionary.
"""














































"""
In this problem, we need to write a Python function that takes a string as input and returns the first non-repeated character in the string. If there are no non-repeated characters