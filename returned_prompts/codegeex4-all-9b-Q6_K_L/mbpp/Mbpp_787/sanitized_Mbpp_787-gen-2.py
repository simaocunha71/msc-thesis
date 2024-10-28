import re
def text_match_three(text):
    return re.match(r"abbb", text) is not None