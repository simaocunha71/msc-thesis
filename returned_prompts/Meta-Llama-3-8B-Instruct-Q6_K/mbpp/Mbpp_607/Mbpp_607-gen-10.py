```
import re
def find_literals(s, pattern):
    match = re.search(pattern, s)
    if match:
        return match.group(), match.start(), match.end()
    return None
```
This function uses the `re` module in Python, which provides support for regular expressions. The `search` function is used to search for the pattern in the string. If a match is found, the `group` method is used to get the matching substring, and the `start` and `end` methods are used to get the start and end indices of the match. If no match is found, the function returns `None`. The unit test provided ensures that the function returns the correct result for the given input. 

For example, when the function is called with the string `'The quick brown fox jumps over the lazy dog.'` and the pattern `'fox'`, it returns the tuple `('fox', 16, 19)`, which means that the pattern `'fox'` was found in the string starting at index 16 and ending at index 19. 

Note that the indices are 0-based, meaning that the first character in the string has an index of 0. 

This function can be used to search for any pattern in a string, not just literals. For example, you could search for a pattern that matches a specific format or a pattern that extracts specific information from the string. 