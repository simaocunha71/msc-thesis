```
def first_non_repeating_character(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in s:
        if char_count[char] == 1:
            return char
    return None
```
Explanation:
The function `first_non_repeating_character` takes a string `s` as input and returns the first non-repeating character in the string. If no non-repeating character is found, it returns `None`.

It first creates a dictionary `char_count` to count the frequency of each character in the string. It then iterates over the string again to find the first character with a count of 1, which is the first non-repeating character. If no such character is found, it returns `None`.

The unit test `assert first_non_repeating_character("abcabc") == None` ensures that the function returns `None` when no non-repeating character is found in the input string. This test covers the edge case where the input string contains only repeating characters. 