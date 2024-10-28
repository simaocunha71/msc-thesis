import re
def text_match_three(s):
    pattern = r"abbb"
    return bool(re.search(pattern, s))