def is_pangram(s):
    return all(letter in s.lower() for letter in map(chr, range(97, 123)))


print(is_pangram('The quick brown fox jumps over the lazy dog'))  # True


"""
Write a python function to find the longest palindrome substring in a given string.
assert longest_palindrome("babad") == "aba"
"""

A: