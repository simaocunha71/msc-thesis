import re
def check_str(s):
    match = re.match(r"^[aeiou]", s, re.IGNORECASE)
    if match:
        return True
    else:
        return False

