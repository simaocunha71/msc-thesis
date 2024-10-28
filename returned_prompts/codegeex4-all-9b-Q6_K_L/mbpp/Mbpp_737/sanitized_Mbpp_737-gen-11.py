import re
def check_str(s):
    pattern = re.compile(r'^[aeiou]')
    return bool(pattern.match(s))