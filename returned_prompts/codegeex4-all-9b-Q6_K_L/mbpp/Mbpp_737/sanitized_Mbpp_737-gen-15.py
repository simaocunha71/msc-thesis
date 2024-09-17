import re
def check_str(s):
    result = re.match(r'^[aeiouAEIOU]', s)
    return result is not None