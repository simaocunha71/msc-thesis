def replace_specialchar(s):
    for ch in ['.', ',', ' ']:
        s = s.replace(ch, ':')
    return s

print(replace_specialchar('Python language, Programming language.'))



