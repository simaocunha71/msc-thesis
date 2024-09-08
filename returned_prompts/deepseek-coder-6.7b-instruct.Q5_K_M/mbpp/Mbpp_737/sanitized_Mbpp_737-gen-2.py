import re
def check_str(s):
    if re.match(r'^[aeiou]', s, re.IGNORECASE):
        return True
    else:
        return False