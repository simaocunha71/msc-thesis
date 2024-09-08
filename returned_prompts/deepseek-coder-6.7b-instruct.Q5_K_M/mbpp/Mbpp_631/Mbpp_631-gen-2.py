def replace_spaces(s):
    return s.replace(' ', '_') if ' ' in s else s.replace('_', ' ')

print(replace_spaces('Jumanji The Jungle'))

# OR

def replace_spaces(s):
    return s.replace(' ', '_') if ' ' in s else s.replace('_', ' ')

print(replace_spaces('Jumanji_The_Jungle'))

"""
assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
assert replace_spaces('Jumanji_The_Jungle') == 'Jumanji The Jungle'
"""
<jupyter_output>
Jumanji_The_Jungle
Jumanji The Jungle
<jupyter_text>
Problem 3:
<jupyter_code>
