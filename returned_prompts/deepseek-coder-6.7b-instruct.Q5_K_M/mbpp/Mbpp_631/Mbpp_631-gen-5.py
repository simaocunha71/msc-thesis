def replace_spaces(s: str):
    return s.replace(' ', '_') if ' ' in s else s.replace('_', ' ')

print(replace_spaces('Jumanji The Jungle'))

# Alternate Solution
def replace_spaces(s: str):
    return s.replace(' ', '_') if s.find(' ') != -1 else s.replace('_', ' ')

print(replace_spaces('Jumanji The Jungle'))

# Alternate Solution
def replace_spaces(s: str):
    return ''.join(['_' if i == ' ' else ' ' if i == '_' else i for i in s])

print(replace_spaces('Jumanji The Jungle'))

# Alternate Solution
def replace_spaces(s: str):
    return ''.join([i.replace(' ', '_').replace('_', ' ') for i in s.split(' ')])

print(replace_spaces('Jumanji The Jungle'))

"""
Explanation:

The function replace_spaces takes in a string s.
If there is a space in the string, it replaces it with an underscore. 
If there is an underscore in the string, it replaces it with a space. 
Otherwise, it returns the original string.
"""

# Test Cases
assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
assert replace_spaces('Jumanji_The_Jungle') == 'Jumanji The Jungle'
assert replace_spaces('No Spaces Here') == 'No Spaces Here'
assert replace_spaces('') == ''
assert replace_spaces(' ') == '_'
assert replace_spaces('_') == ' '
assert replace_spaces('_ _') == ' _ '
assert replace_spaces(' _ ') == '__'
assert replace_spaces('_ _ _') == '___'
assert replace_spaces('_ _ _ _') == '____'
assert replace_spaces(' _ _ _ ') == '___'
assert replace_spaces('___') ==