```
import re
def find_literals(text, pattern):
    matches = re.finditer(pattern, text)
    for match in matches:
        return (match.group(), match.start(), match.end())
```    
The function `find_literals` uses the `re.finditer` function from the `re` module to find all matches of the given `pattern` in the `text`. It then iterates over the matches and returns the first match it finds. The `match.group()` function returns the matched string, `match.start()` returns the start index of the match, and `match.end()` returns the end index of the match. If no match is found, the function will return `None`. The unit test provided ensures that the function returns the correct result for the given input.    
    



