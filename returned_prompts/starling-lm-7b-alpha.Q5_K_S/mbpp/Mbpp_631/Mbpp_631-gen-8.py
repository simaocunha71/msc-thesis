def replace_spaces(string):
    return string.replace(' ', '_').replace('_', ' ')

# assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
# print(replace_spaces('Jumanji The Jungle'))






"""

def replace_spaces(string):
    string_list = list(string)
    for i, char in enumerate(string_list):
        if char == ' ':
            string_list[i] = '_'
        elif char == '_':
            string_list[i] = ' '
    return ''.join(string_list)

print(replace_spaces('Jumanji The Jungle'))

"""

"""

def replace_spaces(string):
    string_list = list(string)
    for i in range(len(string_list)):
        if string_list[i] == ' ':
            string_list[i] = '_'
        elif string_list[i] == '_':
            string_list[i] = ' '
    return ''.join(string_list)

print(replace_spaces('Jumanji The Jungle'))

"""






























































































































































































































