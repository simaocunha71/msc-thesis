def replace_spaces(s):
    return s.replace(' ', '_') if ' ' in s else s.replace('_', ' ')

print(replace_spaces('Jumanji The Jungle'))  # 'Jumanji_The_Jungle'


"""
