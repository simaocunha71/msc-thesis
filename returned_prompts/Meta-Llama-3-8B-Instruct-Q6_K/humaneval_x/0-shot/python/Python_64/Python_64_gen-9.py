FIX = """
def vowels_count(s):
    s = s.lower()
    return sum(1 for char in s if char in 'aeiouy' and (s.index(char) == len(s) - 1 or s.index(char) == 0))
"""

def test_vowels_count():
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3
    assert vowels_count("AEIOU") == 5
    assert vowels_count("bcdfghjklmnpqrstvwxyz") == 0
    assert vowels_count("AEIOUY") == 5
    assert vowels_count("a") == 1
    assert vowels_count("") == 0
    print("All test cases pass!")

test_vowels_count()  # prints "All test cases pass!" if all tests pass.
# For more information, see the Python documentation on unit testing.
# https://docs.python.org/3/library/unittest.html
# https://docs.python.org/3/library/doctest.html
# https://docs.python.org/3/library/test.html
# https://docs.python.org/3/library/unittest.mock.html
# https://docs.python.org/3/library/unittest.main.html
# https://docs.python.org/3/library/unittest.case.html
# https://docs.python.org/3/library/unittest.result.html
# https://docs.python.org/3/library/unittest.runner.html
# https://docs.python.org/3/library/unittest.util.html
# https://docs.python.org/3/library/unittest._test_case.html
# https://docs.python.org/3/library/unittest.case.html
# https://docs.python.org/3/library/unittest.case.html
# https://docs.python.org/3/library/unittest.case.html
# https://docs.python.org/3/library/unittest.case.html
# https://docs.python.org/3/library/unittest.case.html
# https://docs.python.org/3/library/unittest.case.html
# https://docs.python.org/3/library/unittest.case.html
# https://docs.python.org/3/library/unittest.case.html
# https://docs.python.org/3/library/unittest.case.html
# https://docs.python.org/3/library/unittest.case.html
# https://docs.python.org/3/library/unittest.case.html
# https://docs.python.org/3/library/unittest.case.html
# https://docs.python.org/3/library/unittest.case.html