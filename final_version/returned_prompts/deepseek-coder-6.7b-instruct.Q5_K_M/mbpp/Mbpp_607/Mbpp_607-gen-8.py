Here is a Python solution using the `re` module to search for a regex pattern in a string:

```python
import re

def find_literals(string, pattern):
    match = re.search(pattern, string)
    if match:
        return (match.group(), match.start(), match.end())
    else:
        return None
```

This function takes a string and a regex pattern as parameters. It searches the string for the pattern using `re.search`. If a match is found, the function returns a tuple containing the matching substring, the start index and the end index of the match. If no match is found, the function returns `None`.

Test the function with the provided question:

```python
print(find_literals('The quick brown fox jumps over the lazy dog.', 'fox'))
# Output: ('fox', 16, 19)
```

This output means that the substring 'fox' starts at index 16 and ends at index 19 in the string 'The quick brown fox jumps over the lazy dog.'.
"""

# ---------------------
"""
