
import re
def capital_words_spaces(str1):
    return re.sub(r"((?<=[a-z])(?=[A-Z]))", " ", str1)


