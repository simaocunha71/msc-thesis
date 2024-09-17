
def replace_specialchar(s: str) -> str:
    for c in ['.', ',', ' ']:
        s = s.replace(c, ':')
    return s


