def replace_spaces(s):
    if " " in s:
        return s.replace(" ", "_")
    else:
        return s.replace("_", " ")

print(replace_spaces('Jumanji The Jungle'))

# Answer: 'Jumanji_The_Jungle'

# Alternative solution using List comprehension
def replace_spaces(s):
    return ''.join(['_' if i == ' ' else ' ' if i == '_' else i for i in s])

print(replace_spaces('Jumanji_The_Jungle'))

# Answer: 'Jumanji The Jungle'
<jupyter_output>
Jumanji_The_Jungle
Jumanji The Jungle
<jupyter_text>
