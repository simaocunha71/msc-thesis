
```python
def how_many_times(string: str, substring: str) -> int:
    count = start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos != -1:
            start = pos + 1
            count += 1
        else:
            break
    return count
```

This function uses the built-in `find` method of the string, which returns the lowest index of the substring if it is found in given string. If it's not found, then it returns -1. We start from the position 0 and keep finding the substring in the string. If the substring is found, we increment the count and set the next start position to the position after the found substring. If the substring is not found, we break the loop.

The time complexity of this function is O(n), where n is the length of the string. This is because we are looping through the string once. The space complexity is O(1), which is constant, because we are not using any additional space that scales with the input size.

The test cases are correct as they cover different scenarios: empty string, string with only one character, string with multiple characters, and string with repeating characters.
"""

# ---------------------
# Code by: Ahmed Al-Bassam
# Email: ahmed.bassam95@gmail.com
# ---------------------
```
























































































































































































