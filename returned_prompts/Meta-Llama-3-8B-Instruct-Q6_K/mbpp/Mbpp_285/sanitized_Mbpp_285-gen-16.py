import re
def text_match_two_three(text):
    pattern = r"a(b{2,3})"
    if re.fullmatch(pattern, text):
        return True
    return False