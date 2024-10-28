import re

def text_starta_endb(text):
    pattern = re.compile(r"a.*b")
    match = pattern.match(text)
    return match is not None

