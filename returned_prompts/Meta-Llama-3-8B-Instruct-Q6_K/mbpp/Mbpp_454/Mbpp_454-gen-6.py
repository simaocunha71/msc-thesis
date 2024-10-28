You can use the re module in Python to match a word containing 'z'. The function would take a string as an argument and check if it contains a word that has 'z' in it. 

Here's how you can do it:

```
import re

def text_match_wordz(text):
    pattern = r'\b\w*z\w*\b'
    return bool(re.search(pattern, text))
```

This function uses a regular expression pattern to match a word that has 'z' in it. The pattern '\b\w*z\w*\b' means a word boundary, followed by zero or more word characters (letters, numbers, or underscores), followed by 'z', followed by zero or more word characters, and finally a word boundary. The re.search function returns a match object if the pattern is found in the string, or None if it's not. The bool function is used to convert this to a boolean value. 

The unit test `assert text_match_wordz("pythonz.")==True` ensures that the function returns True when the input string contains a word with 'z'. 

This function is case sensitive and it does not consider 'z' as part of a bigger word. For example, it would not match 'xyz' in 'xyzzy', but it would match 'z' in 'z'. If you want to make it case insensitive and consider 'z' as part of a bigger word, you can modify the pattern and function as follows:

```
import re

def text_match_wordz(text):
    pattern = r'\b[[:alpha:]]*z[[:alpha:]]*\b'
    return bool(re.search(pattern, text, re.I))
```

In this modified function, the pattern '[[:alpha:]]*' matches zero or more alphabetic characters, and the re.I flag makes the search case insensitive. This function would match 'z' in 'xyzzy' and 'z' in 'z'. 