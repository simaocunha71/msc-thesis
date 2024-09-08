def replace_specialchar(s):
    for ch in ['.', ',', ' ']:
        if ch in s:
            s = s.replace(ch, ':')
    return s

print(replace_specialchar('Python language, Programming language.'))




