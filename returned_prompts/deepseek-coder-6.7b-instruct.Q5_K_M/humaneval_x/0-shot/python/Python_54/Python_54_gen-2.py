
    def same_chars(s0: str, s1: str):
        return sorted(s0) == sorted(s1)


if __name__ == "__main__":
    import doctest
    doctest.testmod()


"""

def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """
    return sorted(s0) == sorted(s1)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
"""

#tests/test_same_chars.py
import unittest
from same_chars import same_chars

class TestSameChars(unittest.TestCase):
    def test_same_chars(self):
        self.assertEqual(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'), True)
        self.assertEqual(same_chars('abcd', 'dddddddabc'), True)
        self.assertEqual(same_chars('dddddddabc', 'abcd'), True)
        self.assertEqual(same_chars('eabcd', 'dddddddabc'), False)
        self.assertEqual(same_chars('abcd', 'dddddddabce'), False)
        self.assertEqual(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'), False)

if __name__ == '__main__':
    unitt