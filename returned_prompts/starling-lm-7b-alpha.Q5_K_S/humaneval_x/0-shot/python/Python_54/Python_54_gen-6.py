In the same_chars function, you need to check if two strings have the same characters, regardless of the order they appear.

Here are some steps you can follow:

1. Create a function called same_chars that takes two arguments, s0 and s1.
2. Create a dictionary called char_count to store the count of each character in both strings. You can use the keys of the dictionary to store the characters from s0 and s1. The values of the dictionary will be the count of each character.
3. Iterate over each character in s0 and s1 using a for loop. For each character, check if it is present in the char_count dictionary. If it is not present, add it as a new key to the dictionary and set its value to 1. If it is present, increment the value of the key by 1.
4. After counting all the characters, check if the lengths of s0 and s1 are equal. If they are not equal, return False, as the strings cannot have the same characters.
5. Finally, iterate over the keys of the char_count dictionary and check if each key has the same value in the dictionary. If any key does not have the same value as the total count of its occurrences in s0 and s1, return False. Otherwise, return True.

Here's the code for the same_chars function:

```python
def same_chars(s0: str, s1: str):
    char_count = {}
    for char in s0:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    for char in s1:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    if len(s0) != len(s1):
        return False
    for key in char_count:
        if char_count[key] != char_count[key] * 2:
            return False
    return True
```

You can test the function with different inputs to verify that it works correctly. Here are some examples:

```python
print(same_chars('eabcdzz