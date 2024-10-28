import re
def text_starta_endb(s: str):
    return bool(re.match("a.+b$", s))