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
This function first counts the frequency of each character in the string. Then it iterates over the string again to find the first character that has a count greater than 1. If no repeated character is found, it returns None. The unit test `assert first_repeated_char("abcabc") == "a"` ensures that the function works correctly. 





