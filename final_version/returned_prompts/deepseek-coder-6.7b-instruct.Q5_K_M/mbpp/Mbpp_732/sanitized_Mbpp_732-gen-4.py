def replace_specialchar(s):
    special_char = [' ', ',', '.']
    for char in special_char:
        s = s.replace(char, ':')
    return s
s = 'Python language, Programming language.'