

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    distinct_characters = set()
    for char in string:
        if char.isalpha():
            distinct_characters.add(char.lower())
    return len(distinct_characters)


# Here is a step-by-step explanation:

# First, we initialize an empty set, which will store distinct characters.
# Then, we iterate through the given string and add each character to the set,
# but only if the character is an alphabetic one. We convert each character to lowercase,
# because we want to treat uppercase and lowercase characters as the same.
# Finally, we return the length of the set, which gives us the number of distinct characters.
# The time complexity of this solution is O(n), where n is the length of the input string,
# as we iterate through the string exactly once.


# Here are some unit tests to validate the code:

import unittest

class TestCountDistinctCharacters(unittest.TestCase):

    def test_count_distinct_characters(self):
        self.assertEqual(count_distinct_characters('xyzXYZ'), 3)
        self.assertEqual(count_distinct_characters('Jerry'), 4)
        self.assertEqual(count_distinct_characters(''), 0)
        self.assertEqual(count_distinct_characters(' '), 0)
        self.assertEqual(count_distinct_characters('abcdefghijklmnopqrstuvwxyz'), 26)
        self.assertEqual(count_distinct_characters('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 26)
        self.assertEqual(count_distinct_characters('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxy