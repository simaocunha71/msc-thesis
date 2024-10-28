import re
def text_starta_endb(text):
    pattern = r'a.*b$'
    return bool(re.match(pattern, text))