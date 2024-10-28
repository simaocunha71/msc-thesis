import re
def capital_words_spaces(s):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", s)