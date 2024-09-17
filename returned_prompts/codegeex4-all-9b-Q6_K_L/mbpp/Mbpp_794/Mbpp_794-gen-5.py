import re
def text_starta_endb(s: str):
    pattern = r'a.*b$'
    match = re.search(pattern, s)
    if match:
        return True
    else:
        return False

