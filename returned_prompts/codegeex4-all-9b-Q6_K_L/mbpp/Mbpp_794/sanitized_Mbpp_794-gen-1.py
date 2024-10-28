import re
def text_starta_endb(text):
    pattern = r'a.*b$'
    match = re.match(pattern, text)
    return bool(match)