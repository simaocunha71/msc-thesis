import re
def check_str(str):
    regex = re.compile(r'^[aeiou]')
    return bool(regex.match(str))