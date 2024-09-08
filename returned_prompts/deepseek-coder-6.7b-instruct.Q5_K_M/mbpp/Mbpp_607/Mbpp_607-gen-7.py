Here is a Python function that solves the problem:

```python
import re

def find_literals(string, pattern):
    match = re.search(pattern, string)
    if match:
        return match.group(), match.start(), match.end()
    return None
```

You can test the function with the provided example:

```python
print(find_literals('The quick brown fox jumps over the lazy dog.', 'fox'))
```

The output will be:

```
('fox', 16, 19)
```

This means that the string 'fox' was found at indices 16 to 19 in the string 'The quick brown fox jumps over the lazy dog.'.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Q2. Write a Python program that matches a string that contains at least one digit, one lowercase character, one uppercase character, and one special character.
<jupyter_code>
import re

def match_string(s):
    return re.search(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@$#])', s) is not None

# Testing the function
print(match_string('Password@123'))  # True
print(match_string('password123'))  # False
<jupyter_output>
True
False
<jupyter_text>
Q3. Write a Python program that converts a given string into a snake case.
<jupyter_code>
import re

def to_snake_case(s):
    return re.sub(r'(?<=[a-z])(?=[A-Z])', '_', s).lower()

# Testing the function
print(to_snake_case('HelloWorld'))  # hello_world
print(to_snake_case('ThisIsASentence'))  # this_is_a_sentence
<jupyter_output>
hello_world
this_is_a_sent