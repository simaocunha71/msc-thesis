"""
def number_of_substrings(string):
    length = len(string)
    number = (length * (length + 1)) // 2
    return number


def test_number_of_substrings():
    assert number_of_substrings("abc") == 6


test_number_of_substrings()
"""

number_of_substrings = lambda s: (len(s) * (len(s)+1))//2

assert number_of_substrings("abc") == 6

def test_number_of_substrings():
    assert number_of_substrings("abc") == 6


test_number_of_substrings()

# The time complexity of this solution is O(1)

# Here are some corner cases to test:
# assert number_of_substrings("") == 0

# assert number_of_substrings("a") == 1

# assert number_of_substrings("ab") == 3

# assert number_of_substrings("abcdefghijklmnopqrstuvwxyz") == 3628800


# Here are some edge cases to test:
# assert number_of_substrings("a" * 10 ** 9) == 5 * 10 ** 9

# assert number_of_substrings("a" * 10 ** 18) == 5000000000000000000

# assert number_of_substrings("a" * 10000) == 5000 * 10000

# assert number_of_substrings("ab" * 10000) == 3 * 10000 ** 2

# assert number_of_substrings("abc" * 10000) == 6 * 10000 ** 2

# assert number_of_substrings("abcdefghijklmnopqrstuvwxyz" * 10000) == 3628800 * 10000

# assert number_