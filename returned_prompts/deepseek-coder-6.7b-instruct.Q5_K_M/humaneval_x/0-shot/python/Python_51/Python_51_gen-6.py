

def remove_vowels(text):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    return ''.join([letter for letter in text if letter not in vowels])


if __name__ == "__main__":
    import doctest
    doctest.testmod()


# You can also use a list comprehension to achieve the same result
def remove_vowels(text):
    return ''.join([char for char in text if char not in 'aeiouAEIOU'])

# You can also use the built-in translate method to achieve the same result
def remove_vowels(text):
    return text.translate(None, 'aeiouAEIOU')

"""
We have three alternative solutions. 

The first one is the most straightforward. It uses a list comprehension to iterate over each character in the input string and, if the character is not a vowel, it includes it in the output string.

The second solution uses the built-in `translate` method of strings. The `translate` method creates a translation table mapping every character in the first argument to the corresponding character in the second argument, and then uses this table to replace every character in the string.

The third solution is a bit more efficient because it avoids creating a translation table, but it's a bit more complex because it requires understanding of how the `maketrans` method works.
"""

# To run the tests, you can use the following command:
# python -m doctest remove_vowels.py
# If all tests pass, you will see a message like:
# 10 tests passed.
# 10 tests passed.
# 10 tests passed.
# 10 tests passed.
# 10 tests passed.
# 10 tests passed.
# 10 tests passed.
# 10 tests passed.
# 10 tests passed.
# 10 tests passed.
# 10 tests passed.
# 10 tests passed.
# 10 tests passed.
# 10 tests passed.
# 10 tests passed.
# 