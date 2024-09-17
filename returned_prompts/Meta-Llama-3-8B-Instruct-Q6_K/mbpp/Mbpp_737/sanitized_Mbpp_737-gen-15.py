import re
def check_str(s):
    pattern = re.compile('^[aeiouAEIOU]')  # ^ means start of the string
    if pattern.match(s):
        return True
    else:
        return False