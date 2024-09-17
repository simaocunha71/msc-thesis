import re
def check_str(s):
    match = re.match(r'^[aeiouAEIOU]', s)
    if match:
        return True
    else:
        return False