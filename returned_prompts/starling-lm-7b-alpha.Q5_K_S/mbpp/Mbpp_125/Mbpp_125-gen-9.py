"""
def find_length(s):
    max_diff = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if s[i:j].count('0') > s[i:j].count('1'):
                max_diff = max(max_diff, s[i:j].count('0') - s[i:j].count('1'))
            else:
                max_diff = max(max_diff, s[i:j].count('1') - s[i:j].count('0'))
    return max_diff
"""

def find_length(s):
    max_diff = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            max_diff = max(max_diff, abs(s[i:j].count('0') - s[i:j].count('1')))
    return max_diff

# assert find_length("11000010001") == 6

```
This function finds the maximum difference between the number of 0s and the number of 1s in any sub-string of the given binary string by iterating through all possible sub-strings. It checks if the count of 0s is greater than the count of 1s in the sub-string, and if so, updates the maximum difference accordingly. If the count of 1s is greater, it does the same but with the counts of 1s and 0s swapped. Finally, it returns the maximum difference found.
```

```
"""
def find_length(s):
    max_diff = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            max_diff = max(max_diff, abs(s[i:j].count('0') - s[i:j].count('1')))
    return max_diff

# assert find_length("11000010001") == 6
```

This code defines a