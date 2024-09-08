import re
def text_match_three(s):
    if re.match(r"abbb", s):
        return True
    else:
        return False