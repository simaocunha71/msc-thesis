```
def count_char_position(s):
    count = 0
    for i in range(len(s)):
        if ord(s[i].lower()) - 97 == i:
            count += 1
    return count
```

# This function works by iterating over the input string and checking if the character's ASCII value minus 97 (the ASCII value of 'a') is equal to the index of the character in the string. This is done in a case-insensitive manner by converting the character to lowercase using the `lower()` method. If the condition is true, the count is incremented by 1.

# The function returns the count of characters that occur at the same position in the string as in the English alphabet.

# Example usage:
# print(count_char_position("xbcefg"))  # Output: 2

```python
```