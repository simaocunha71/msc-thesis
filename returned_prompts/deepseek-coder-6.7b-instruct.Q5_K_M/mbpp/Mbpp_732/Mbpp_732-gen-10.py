
def replace_specialchar(s):
    for c in ['.',',',' ']:
        s = s.replace(c, ':')
    return s


