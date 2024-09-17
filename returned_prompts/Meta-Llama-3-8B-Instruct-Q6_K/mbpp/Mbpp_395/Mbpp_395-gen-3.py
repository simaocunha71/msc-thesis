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
The function first counts the occurrences of each character in the string using a dictionary. Then it iterates over the string again and returns the first character that has a count of 1. If no such character is found, it returns None. The unit test `assert first_non_repeating_character("abcabc") == None` ensures that the function returns None when there is no non-repeating character in the string. 

This function has a time complexity of O(n), where n is the length of the input string, because it iterates over the string twice. The space complexity is also O(n), as in the worst case, it needs to store each character in the dictionary. 





```python
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





The provided code defines a function `first_non_repeating_character` that takes a string `s` as input and returns the first non-repeating character in the string. If no such character is found, it returns `None`.

Here's a step-by-step breakdown of how the function works:

1. It initializes an empty dictionary `char_count` to store the count of each character in the string.
2. It iterates over the string `s` and updates the `char_count` dictionary. For each character, it checks if the character is already in the dictionary. If it is, it increments the count by 1. If it's not, it sets the count to 1.
3. It iterates over the string `s` again and checks each character's count in the `char_count` dictionary. If a character has a count of 1, it means it's the first non-repeating character, so the function returns that character.
4. If no non-repeating character is found, the function returns `None`.

The unit test `assert first_non_repeating_character