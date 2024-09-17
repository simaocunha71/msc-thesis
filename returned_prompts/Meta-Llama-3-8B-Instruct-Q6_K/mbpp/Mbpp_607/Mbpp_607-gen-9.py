```
import re

def find_literals(text, pattern):
    match = re.search(pattern, text)
    if match:
        return match.group(), match.start(), match.end()
    return None
```
This function uses Python's built-in `re` module to search for the regex pattern in the given text. The `re.search` function returns a match object if the pattern is found, or `None` if it's not. If a match is found, the function returns the matching substring (`match.group()`), the start index of the match (`match.start()`) and the end index of the match (`match.end()`). If no match is found, the function returns `None`. 

The unit test `assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)` ensures that the function returns the correct values when a match is found. It checks if the function returns a tuple containing the string 'fox', the start index 16 and the end index 19 when searching for the pattern 'fox' in the given text.  If the function returns the correct values, the test passes. If not, it raises an AssertionError. 