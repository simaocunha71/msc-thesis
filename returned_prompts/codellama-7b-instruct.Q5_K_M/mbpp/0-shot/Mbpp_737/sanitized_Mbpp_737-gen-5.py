import re
def check_str(name):
    pattern = r"^[aeiouAEIOU]"
    if re.match(pattern, name):
        return True
    else:
        return False