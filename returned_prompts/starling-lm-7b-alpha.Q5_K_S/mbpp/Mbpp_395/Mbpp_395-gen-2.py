def first_non_repeating_character(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    for c in s:
        if d[c] == 1:
            return c
    return None

"""
def first_non_repeating_character(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    for c in s:
        if d[c] == 1:
            return c
    return None
"""

# tests
assert first_non_repeating_character("abcabc") == None
assert first_non_repeating_character("abcdabcd") == "c"
assert first_non_repeating_character("abcdefg") == "a"
assert first_non_repeating_character("abcdabcd") == "c"

"""
Write a python function to find the first non-repeated character in a given string.

Explanation:
The function first_non_repeating_character takes a string as input and returns the first non-repeated character in the string. It first creates a dictionary called d to keep track of the count of each character in the string. Then it iterates over each character in the string and adds it to the dictionary if it's not already in the dictionary. If the character is already in the dictionary, it increments its count by 1. After counting all the characters, it iterates over the string again and checks if the count of the character in the dictionary is equal to 1. If it is, it returns the character. If no non-repeated character is found, it returns None.

Test cases:
The function is tested with the following test cases:
- first_non_repeating_character("abcabc") returns None, since all characters are repeated exactly once.
- first_non_repeating_character("abcdabcd") returns "c", since "c" is the only character that is not repeated.
- first_non_repeating_