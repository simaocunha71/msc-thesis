
import re
def text_starta_endb(txt: str) -> bool:
    pattern = "^a.*b$"
    if re.match(pattern, txt):
        return True
    else:
        return False


