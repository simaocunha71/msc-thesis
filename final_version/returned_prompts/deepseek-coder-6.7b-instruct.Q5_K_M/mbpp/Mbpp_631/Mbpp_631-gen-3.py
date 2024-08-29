def replace_spaces(s):
    return s.replace(' ', '_') if ' ' in s else s.replace('_', ' ')

print(replace_spaces('Jumanji The Jungle'))  # Jumanji_The_Jungle

"""
Alternative solution using list comprehension:
"""

def replace_spaces_v2(s):
    return ''.join(['_' if char == ' ' else ' ' if char == '_' else char for char in s])

print(replace_spaces_v2('Jumanji The Jungle'))  # Jumanji_The_Jungle

"""
This solution works by iterating over the string and replacing spaces with underscores and vice versa at each character.
"""

# assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
# assert replace_spaces_v2('Jumanji_The_Jungle') == 'Jumanji The Jungle'
<jupyter_output>
Jumanji_The_Jungle
<jupyter_text>
Question 3:
<jupyter_code>
