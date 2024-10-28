import re
def text_match_three(text):
    pattern = r"abbb"
    return re.match(pattern, text) is not None