```
import re

def find_literals(text, pattern):
    match = re.search(pattern, text)
    if match:
        return match.group(), match.start(), match.end()
    else:
        return None, None, None
```


The function uses the `re.search` function from the `re` module to search for the pattern in the text. If a match is found, it returns the matching substring, the start index, and the end index of the match. If no match is found, it returns `None` for all three values.

The unit test `assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)` ensures that the function correctly finds the match and returns the expected values.