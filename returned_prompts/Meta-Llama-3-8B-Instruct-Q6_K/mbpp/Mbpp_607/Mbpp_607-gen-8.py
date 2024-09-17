```
import re

def find_literals(s, pattern):
    match = re.search(pattern, s)
    if match:
        return match.group(), match.start(), match.end()
    else:
        return None
``` 
The function `find_literals` takes two parameters: `s` (the string to search) and `pattern` (the regex pattern to search for). It uses the `re.search` function from the `re` module to find the first occurrence of the pattern in the string. If a match is found, it returns a tuple containing the matched substring, the start index, and the end index. If no match is found, it returns `None`. The unit test provided ensures that the function works correctly. 

The unit test:
```
assert find_literals('The quick brown fox jumps over the lazy dog.', 'fox') == ('fox', 16, 19)
``` 
This test checks that the function returns the correct matched substring, start index, and end index when the pattern 'fox' is found in the string 'The quick brown fox jumps over the lazy dog.'. The expected output is a tuple containing the string 'fox', the start index 16, and the end index 19. 

The function can be used to search for any regex pattern in a string. For example, you can use it to find all occurrences of a word in a text, or to extract specific information from a log file. It's a powerful tool for working with text data in Python. 

Note: The `re.search` function returns a `match` object, which has several useful methods and attributes. The `group` method returns the matched substring, the `start` method returns the start index of the match, and the `end` method returns the end index of the match. The function `find_literals` uses these methods to extract the desired information from the match object. 

This function is case-sensitive, so it will only find matches if the pattern and the string are in the same case. If you want to perform a case-insensitive search, you can use the `re.IGNORECASE` flag when compiling the regex pattern. For example:
```
pattern = re.compile(pattern, re.IGNORECASE)
match = pattern.search(s)
``` 
This will make the function ignore the case of the pattern and the string when searching for matches. 
```python
import re

def find_literals(s, pattern):
    pattern = re.compile(pattern)
    match = pattern.search(s)
    if match:
