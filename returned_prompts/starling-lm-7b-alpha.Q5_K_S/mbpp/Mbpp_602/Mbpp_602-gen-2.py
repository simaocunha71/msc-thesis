def first_repeated_char(s):
    for c in s:
        if s.count(c) > 1 and s.index(c) == s.index(c, s.index(c)+1):
            return c
    return None

# Test
print(first_repeated_char("abcabc")) # "a"
print(first_repeated_char("abcdef")) # None

"""
Explanation:
The function first_repeated_char(s) is implemented by iterating through each character in the given string. For each character c, the function first checks if the count of c in the string is greater than 1 (i.e. it is a repeated character), and second checks if the first occurrence of c is also the first occurrence of c in the remaining part of the string. If both conditions are true, the function returns c, indicating that it is the first repeated character in the string. If no repeated character is found, the function returns None.

The time complexity of the function is O(n^2), where n is the length of the string, because for each character in the string, the function needs to count the number of occurrences of the character and find its first occurrence in the remaining part of the string, which takes O(n) time in total. The space complexity of the function is O(n), because the function needs to store the string and the count of each character, which takes a total of O(n) space.
"""

# Alternative implementation:
def first_repeated_char(s):
    char_count = {}
    for c in s:
        if c in char_count:
            return c
        char_count[c] = 1
    return None

# Test
print(first_repeated_char("abcabc")) # "a"
print(first_repeated_char("abcdef")) # None

"""
Explanation:
The function first_repeated_char(s) is implemented by maintaining a dictionary char_count to count the number of occurrences of each character in the given string. For each character c in the string, the function first checks if c is already in char_count. If it is, it means c is a repeated character, and the function returns c. If