```
import re

def find_literals(text, pattern):
    match = re.search(pattern, text)
    if match:
        return match.group(), match.start(), match.end()
    else:
        return None
```


This function uses the `re.search` function from the `re` module to search for the first occurrence of the pattern in the text. If a match is found, it returns the matched substring, start index, and end index. If no match is found, it returns `None`. The `match.group()` returns the matched substring, `match.start()` returns the start index of the match, and `match.end()` returns the end index of the match. The `assert` statement is used to test the function with the given example.