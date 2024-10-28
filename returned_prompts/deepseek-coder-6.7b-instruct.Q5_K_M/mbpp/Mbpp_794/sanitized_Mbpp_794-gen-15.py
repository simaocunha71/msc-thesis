import re
def text_starta_endb(text):
    return re.match('a.*b$', text) is not None