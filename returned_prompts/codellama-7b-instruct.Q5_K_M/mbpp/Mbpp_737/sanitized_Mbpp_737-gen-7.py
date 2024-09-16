import re
def check_str(given_str):
    pattern = r"a|e|i|o|u"
    if re.match(pattern, given_str):
        return True
    else:
        return False