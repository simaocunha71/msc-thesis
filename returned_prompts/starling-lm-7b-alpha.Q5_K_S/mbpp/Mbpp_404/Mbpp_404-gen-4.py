def is_palindrome(s):
    return s == s[::-1]

# assert is_palindrome("madam") == True
# assert is_palindrome("noon") == True
# assert is_palindrome("hello") == False


"""
Write a python function to check if a string is a permutation of another string.
assert is_permutation("abc","bac") == True
assert is_permutation("abc","bacd") == False
"""

A: