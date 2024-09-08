def check_str(s):
    import re
    return bool(re.match(r'^[aeiou]', s, re.I))