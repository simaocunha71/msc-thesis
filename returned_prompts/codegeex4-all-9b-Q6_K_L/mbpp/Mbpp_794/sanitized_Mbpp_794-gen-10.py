import re
def text_starta_endb(s):
    pattern = r'a.*b$'
    return bool(re.match(pattern, s))