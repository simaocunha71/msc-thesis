"""
Write a python function to find the first non-repeated character in a given string.
assert first_non_repeating_character("abcabc") == None
"""
# Solution 1: Using List Comprehension
def first_non_repeating(string):
    return [char for char in list(set(string))] # Convert set of chars to string

print(first_non_repeating("abcabc"))