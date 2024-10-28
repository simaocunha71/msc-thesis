import re
def check_str(string):
    return bool(re.match(r'^[aeiou]', string, re.IGNORECASE))