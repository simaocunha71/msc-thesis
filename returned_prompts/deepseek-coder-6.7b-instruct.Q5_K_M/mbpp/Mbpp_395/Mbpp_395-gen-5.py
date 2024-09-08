def first_non_repeating_character(s: str):
    for i in s:
        if s.count(i) == 1:
            return i
    return None

print(first_non_repeating_character("abcabc"))

"""
Here is the solution:
The function first_non_repeating_character() takes a string as input and iterates over each character in the string. 
For each character, it counts the number of times it appears in the string using the count() method. 
If the count is 1, it means that the character does not repeat in the string, so it returns the character. 
If it goes through the entire string without finding a character that does not repeat, it returns None.
"""

"""
Here's a more optimized version of the function using a dictionary to keep track of the characters that have already been seen. 
This version has a time complexity of O(n), where n is the length of the string.
"""

def first_non_repeating_character(s: str):
    count_dict = {}
    for char in s:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    for char in s:
        if count_dict[char] == 1:
            return char
    return None

print(first_non_repeating_character("abcabc"))

"""
The function first_non_repeating_character() takes a string as input and iterates over each character in the string. 
For each character, it updates the count of the character in the count_dict dictionary. 
Then it iterates over the string again and returns the first character that has a count of 1 in the count_dict dictionary. 
If it goes through the entire string without finding a character that does not repeat, it returns None.
"""

"""
Test Cases:

assert first_non_repeating_character("abcabc") == None
assert first_non_repeating_character("abc") == "a"
assert first_non_repeating_character("aabbcc") == None
assert first_non_repeating_character("aab