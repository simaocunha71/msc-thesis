Here is a Python solution using the `re` library:

```python
import re

def find_literals(text, pattern):
    match = re.search(pattern, text)
    if match:
        return match.group(), match.start(), match.end()
    return None

print(find_literals('The quick brown fox jumps over the lazy dog.', 'fox'))
```

This function takes a text string and a pattern string as input, and returns a tuple containing the matched substring, the start index of the match, and the end index of the match. The `re.search()` function is used to search the text for the pattern, and the `group()`, `start()`, and `end()` methods of the resulting `Match` object are used to get the matched substring, start index, and end index.

The function returns `None` if there is no match.
"""

def test_find_literals():
    assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)
    assert find_literals('Hello, world.', 'world') == ('world', 7, 12)
    assert find_literals('Python is fun.', 'jump') is None

test_find_literals()
"""
This function `test_find_literals()` tests the `find_literals()` function with some test cases. The expected output of the function should match the expected output in the comments.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
**Question 3** 