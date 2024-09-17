You can solve this problem as follows:

```python
def count_char_position(s):
    s = s.lower()
    count = 0
    for i in range(len(s)):
        if ord(s[i]) - 96 == i + 1:
            count += 1
    return count
```




```python
def count_char_position(s):
    s = s.lower()
    count = 0
    for i in range(len(s)):
        if ord(s[i]) - 96 == i + 1:
            count += 1
    return count
```


This solution works as follows:

- Convert the string to lowercase to make the comparison case-insensitive.
- Initialize a counter to keep track of the number of characters that occur at the same position in the string as in the English alphabet.
- Iterate over the characters in the string.
- For each character, check if the ASCII value of the character minus 96 (the ASCII value of 'a') equals the current position plus 1.
- If the condition is met, increment the counter.
- Return the count at the end.