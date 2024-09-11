"""
def first_repeated_char(str):
    dict = {}
    for char in str:
        if char in dict:
            return char
        else:
            dict[char] = 1
    return None

print(first_repeated_char("abcabc"))
"""

def first_repeated_char(str):
    dict = {}
    for char in str:
        if char in dict:
            return char
        else:
            dict[char] = 1
    return None

print(first_repeated_char("abcabc"))


"""
The function works by iterating over the given string and for each character in the string, checks if it is already in the dictionary. If the character is already in the dictionary, it is a repeated character and the function returns it. If the character is not already in the dictionary, it adds the character to the dictionary. If the function has gone through the entire string without finding a repeated character, it returns None.

The function uses a dictionary to keep track of the characters it has already seen. This allows it to determine if a character is repeated or not in constant time (O(1)).
"""

"""
To make the code more efficient, we can use a set instead of a dictionary to keep track of the characters. This will reduce the time complexity of checking if a character is in the set from O(1) to O(log n). Here is the updated function using a set:
"""

def first_repeated_char(str):
    set = set()
    for char in str:
        if char in set:
            return char
        else:
            set.add(char)
    return None

print(first_repeated_char("abcabc"))

"""
This function is more efficient than the previous one because checking if a character is in a set is faster than checking if it is in a dictionary. The time complexity of this function is O(n log n), where n is the length of the string.
"""

"""
Here's a more concise version of the function that achieves the same result:
"""

def first_repeated_char(str):
    return next((char for char in str if str.index(char) != str.rindex(char)), None