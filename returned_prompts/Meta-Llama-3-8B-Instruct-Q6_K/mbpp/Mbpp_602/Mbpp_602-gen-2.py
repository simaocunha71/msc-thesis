```
def first_repeated_char(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in s:
        if char_count[char] > 1:
            return char
    return None
```
This function works by first creating a dictionary `char_count` where the keys are the characters in the string and the values are the counts of each character. Then it iterates over the string again, and returns the first character that has a count greater than 1. If no repeated character is found, it returns `None`. The unit test `assert first_repeated_char("abcabc") == "a"` ensures that the function returns the first repeated character in the string. 

The time complexity of this function is O(n), where n is the length of the string, because it makes two passes over the string. The space complexity is also O(n), because in the worst case it has to store every character in the dictionary. 