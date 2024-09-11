"""
To extract values between quotation marks, we can use the `re` module to split the string.

Here's how you can do this:

```python
import re

def extract_quotation(s):
    return re.findall('"(.*?)"', s)
```

The `re.findall` function returns all non-overlapping matches of pattern in string, as a list of strings.
The string is scanned left-to-right, and matches are returned in the order found.
If one or more groups are present in the pattern, return a list of groups; otherwise, return a list of complete matches.

The pattern `"(.*?)"` matches any character (except a newline, due to Python’s `re` module) zero or more times, but as few times as possible, expanding the smallest amount possible.
The `"(.*?)"`, inside the quotes, is a capturing group that matches any character, any number of times, and as few times as possible.

You can use this function like this:

```python
print(extract_quotation('Cortex "A53" Based "multi" tasking "Processor"'))  # prints: ['A53', 'multi', 'Processor']
```
"""

code= """
import re

def extract_quotation(s):
    return re.findall('"(.*?)"', s)
"""

exec(code)

assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']











































































































































