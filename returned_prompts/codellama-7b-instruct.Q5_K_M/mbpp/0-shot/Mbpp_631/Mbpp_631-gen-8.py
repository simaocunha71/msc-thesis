def replace_spaces(string):
    return string.replace(' ', '_').replace('_', ' ')

# Tests
assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
assert replace_spaces('The Jungle Book') == 'The_Jungle_Book'
