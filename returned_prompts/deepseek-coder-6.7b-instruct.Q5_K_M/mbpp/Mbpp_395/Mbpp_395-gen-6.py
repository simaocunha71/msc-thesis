"""
Here is a solution for the problem:

We can use a dictionary to store the frequency of characters in the string. Then we iterate through the string again, this time checking the dictionary for the frequency of each character. The first character with a frequency of 1 is the first non-repeating character.

"""

def first_non_repeating_character(s):
    character_frequency = {}

    # Get the frequency of each character in the string
    for char in s:
        if char in character_frequency:
            character_frequency[char] += 1
        else:
            character_frequency[char] = 1

    # Check the string again to find the first non-repeating character
    for char in s:
        if character_frequency[char] == 1:
            return char

    return None

assert first_non_repeating_character("abcabc") == None

# Test case
assert first_non_repeating_character("aabbcc") == None
assert first_non_repeating_character("aabbccd") == "d"
assert first_non_repeating_character("abcabcdef") == "d"
assert first_non_repeating_character("abcdef") == "a"
"""

