def replace_specialchar(s):
    specialchars = [" ", ",", "."]
    for char in specialchars:
        s = s.replace(char, ":")
    return s