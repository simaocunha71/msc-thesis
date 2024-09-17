
import re
def text_match_wordz_middle(text):
    pattern = r"^[^z]*z[^z]*$"
    return bool(re.match(pattern, text))


