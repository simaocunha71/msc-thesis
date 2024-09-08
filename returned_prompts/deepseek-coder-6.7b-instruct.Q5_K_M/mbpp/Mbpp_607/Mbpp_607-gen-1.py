You can use the `re` module in Python to perform regex operations.

```python
import re

def find_literals(string, pattern):
    match = re.search(pattern, string)
    if match:
        return match.group(), match.start(), match.end()
    return None

print(find_literals('The quick brown fox jumps over the lazy dog.', 'fox'))
```
This will return `('fox', 16, 19)`. 

In the `find_literals` function, the `re.search` function is used to search the string for the regex pattern. The `match.group()` function is used to get the matched substring, `match.start()` to get the start index and `match.end()` to get the end index. 

The `re.search` function will return a match object if the pattern is found in the string. If not, it will return `None`.



