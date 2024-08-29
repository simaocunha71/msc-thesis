def check_str(s):
    import re
    pattern = '^[aeiou]'
    if re.match(pattern, s):
        return True
    else:
        return False