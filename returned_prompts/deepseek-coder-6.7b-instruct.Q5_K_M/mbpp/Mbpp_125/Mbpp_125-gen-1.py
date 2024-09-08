Here is the Python solution for the problem:

```python
def find_length(s):
    # Initialize difference and counts of 0s and 1s
    max_diff = count_0 = count_1 = 0

    # Traverse through every character of given string
    for i in range(len(s)):

        # If s[i] is 0, increment count_0
        if s[i] == '0':
            count_0 += 1

        # If s[i] is 1, increment count_1 and update max_diff
        else:
            count_1 += 1
            max_diff = max(max_diff, count_1 - count_0)

    return max_diff

# Test the function
print(find_length("11000010001"))  # Expected output: 6
```

The function `find_length` traverses the string `s` and keeps track of the count of 0s and 1s. For every character in the string, it checks whether it's a 0 or a 1. If it's a 0, it increases the count of 0s. If it's a 1, it increases the count of 1s and updates the maximum difference between the count of 0s and 1s. Finally, it returns the maximum difference.

The function `find_length` has a time complexity of O(n), where n is the length of the string `s`, because it traverses the string only once.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2
<jupyter_code>
"""
