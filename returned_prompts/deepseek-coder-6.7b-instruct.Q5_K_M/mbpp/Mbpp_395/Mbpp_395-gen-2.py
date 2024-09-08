def first_non_repeating_character(s):
    count = {}
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    for char in s:
        if count[char] == 1:
            return char
    return None

print(first_non_repeating_character("abcabc")) # None
"""
The function works by first creating a dictionary that keeps track of the count of each character in the string. 
Then it iterates through the string again and returns the first character that has a count of 1.
"""

# 