import re
def capital_words_spaces(txt):
    return re.sub(r"((?<=[a-z])(?=[A-Z]))", " ", txt)