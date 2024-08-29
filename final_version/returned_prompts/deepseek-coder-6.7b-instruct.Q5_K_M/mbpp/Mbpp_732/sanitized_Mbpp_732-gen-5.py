def replace_specialchar(s):
    for ch in ['.', ',', ' ']:
        s = s.replace(ch, ':')
    return s