import re
def check_str(txt):
    return bool(re.match("^[aeiou]", txt))