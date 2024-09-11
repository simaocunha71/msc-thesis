def replace_spaces(s):
    s_list = list(s)
    for i in range(len(s_list)):
        if s_list[i] == ' ':
            s_list[i] = '_'
    return ''.join(s_list)

# Testing
assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
assert replace_spaces('Hello World') == 'Hello_World'
assert replace_spaces('') == ''

# Replacing underscores with spaces
def replace_underscores(s):
    s_list = list(s)
    for i in range(len(s_list)):
        if s_list[i] == '_':
            s_list[i] = ' '
    return ''.join(s_list)

# Testing
assert replace_underscores('Jumanji_The_Jungle') == 'Jumanji The Jungle'
assert replace_underscores('Hello_World') == 'Hello World'
assert replace_underscores('') == ''






"""
"""

```
def replace_spaces(s):
    s_list = list(s)
    for i in range(len(s_list)):
        if s_list[i] == ' ':
            s_list[i] = '_'
    return ''.join(s_list)

def replace_underscores(s):
    s_list = list(s)
    for i in range(len(s_list)):
        if s_list[i] == '_':
            s_list[i] = ' '
    return ''.join(s_list)
```

This code defines two functions, `replace_spaces` and `replace_underscores`, that replace whitespaces with an underscore and vice versa in a given string, respectively. The `replace_spaces` function iterates through a list of characters in the input string `s`, and if a whitespace is encountered, it replaces it with an underscore. The modified list of characters is then joined back into a string and returned.