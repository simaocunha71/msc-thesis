def replace_specialchar(str):
    str = str.replace(" ", ":")
    str = str.replace(",", ":")
    str = str.replace(".", ":")
    return str


# Another way
def replace_specialchar(str):
    return str.replace(" ", ":").replace(",", ":").replace(".", ":")


# Test
assert replace_specialchar('Python language, Programming language.')==('Python:language::Programming:language:')
#assert replace_specialchar('Python,language')==('Python:language:')

"""
Also, you can use regular expressions to replace all special characters, but it's a bit too much.
"""

# Python3
import re
def replace_specialchar(str):
    return re.sub(r'[ ,.]', ':', str)
```