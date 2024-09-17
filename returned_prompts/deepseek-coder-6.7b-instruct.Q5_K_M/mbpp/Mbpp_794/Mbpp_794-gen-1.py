
import re
def text_starta_endb(txt):
    return bool(re.fullmatch(r'a.*b$', txt))


