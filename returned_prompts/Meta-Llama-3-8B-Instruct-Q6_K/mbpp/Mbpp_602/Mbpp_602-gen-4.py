```
def first_repeated_char(s):
    char_count = {}
    for char in s:
        if char in char_count:
            return char
        char_count[char] = 1
    return None
```
This function iterates over the string, and for each character, it checks if it's already in the `char_count` dictionary. If it is, it means this character has been seen before, so it returns the character. If it's not, it adds the character to the dictionary with a count of 1. If no repeated character is found, it returns `None`.

The unit test `assert first_repeated_char("abcabc") == "a"` ensures that the function returns the first repeated character in the string. 

This function has a time complexity of O(n), where n is the length of the string, because it needs to iterate over the entire string to find the first repeated character. The space complexity is O(1), because it uses a constant amount of space to store the character count dictionary, regardless of the size of the input string. 