def first_repeated_char(s):
    d = {}
    for c in s:
        if c in d:
            return c
        d[c] = 1
    return "No repeated character"


# Test Cases
print(first_repeated_char("abcabc"))  # a
print(first_repeated_char("abcde"))  # No repeated character




















"""
Explanation:
The function works by using a dictionary to keep track of each character's first occurrence.
It iterates through the string, checking if a character is in the dictionary. If it is, it returns that character,
as it is a repeated character. If the character is not in the dictionary, it adds it to the dictionary.
If the loop finishes without finding a repeated character, the function returns "No repeated character".

"""

"""
The time complexity of this function is O(n), where n is the length of the string.
The space complexity is O(1), as the dictionary will only grow at most linearly with the size of the string.
"""

"""
Test Cases:
The provided test cases demonstrate that the function correctly identifies the first repeated character in a string,
and also correctly returns "No repeated character" if there are no repeated characters.
"""

"""
Alternative Solutions:
There are multiple ways to solve this problem. Here are a few alternatives:

1. Using a Set: Instead of a dictionary, the function could use a set to keep track of the characters. Sets are unordered,
which means the first occurrence of a character might not necessarily be the first element in the set. This would require
iterating through the set to find the first occurrence of a character. However, since sets are implemented as hash tables,
the time complexity of adding and checking a character in a set would be constant time, O(1), making this solution faster
than using a dictionary.

2. Using a Counter: The Python `collections` module provides a `Counter` class, which is a dictionary subclass that counts
the occurrences of its elements. This would simplify the function to:

def first_repeated_char(s):
    c =