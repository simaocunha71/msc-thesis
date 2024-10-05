```python
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    max_length = max(len(s) for s in strings)
    for s in strings:
        if len(s) == max_length:
            return s
```

# Explanation

1. **Input Check**: We first check if the input list `strings` is empty. If it is, we return `None` because there are no strings to compare.

2. **Finding Maximum Length**: We use a generator expression `(len(s) for s in strings)` to find the length of each string in the list. We then use the `max` function to find the maximum length among all strings.

3. **Finding Longest String**: We iterate over the list of strings again. For each string, we check if its length is equal to the maximum length found in step 2. If it is, we return that string. If there are multiple strings with the same maximum length, we return the first one we encounter.

This solution is efficient because it only requires two passes over the list of strings. The first pass is used to find the maximum length, and the second pass is used to find the longest string.