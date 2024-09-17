import re
def check_str(s: str) -> bool:
    if re.match(r'^[aeiou]', s.lower()):
        return True
    else:
        return False