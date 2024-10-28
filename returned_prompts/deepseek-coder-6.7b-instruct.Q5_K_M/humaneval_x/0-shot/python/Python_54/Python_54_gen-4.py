

def same_chars(s0: str, s1: str) -> bool:
    return sorted(s0) == sorted(s1)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

# The function sorted() returns a list of the characters in the string, sorted in ascending order. 
# Therefore, if two strings are anagrams of each other, their sorted lists will be identical. 
# We can therefore compare these sorted lists using the == operator.
</code></pre>

</body>
</html>
""",
        )


class TestCheckAnagrams(unittest.TestCase):
    maxDiff = None

    def test_check_anagrams(self):
        tests = [
            ("eabcdzzzz", "dddzzzzzzzddeddabc", True),
            ("abcd", "dddddddabc", True),
            ("dddddddabc", "abcd", True),
            ("eabcd", "dddddddabc", False),
            ("abcd", "dddddddabce", False),
            ("eabcdzzzz", "dddzzzzzzzddddabc", False),
        ]

        for test in tests:
            with self.subTest(test=test):
                self.assertEqual(
                    same_chars(test[0], test[1]),
                    test[2],
                )


if __name__ == "__main__":
    unittest.main()

#python_tests/test_check_palindrome.py
import unittest
from main import is_palindrome


class TestCheckPalindrome(unittest.TestCase):
    maxDiff = None

    def test_check_palindrome(self):
        tests = [
            ("radar", True),
            ("python", False),
            ("a", True),
            ("", True),
            ("aa", True),
            ("ab", False),
            ("madam", True),
            ("anaconda", False),
        ]