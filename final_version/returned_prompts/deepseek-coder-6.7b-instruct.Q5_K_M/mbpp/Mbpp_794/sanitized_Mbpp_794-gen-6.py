import re
def text_starta_endb(string):
    pattern = "a.*b$"
    if re.search(pattern, string):
        return True
    else:
        return False