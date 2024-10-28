import re
def check_str(s):
    if re.match('^[aeiouAEIOU].*', s):
        return True
    else:
        return False