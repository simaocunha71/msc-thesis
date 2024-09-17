import re
def check_str(string):
    pattern = "[AEIOUaeiou]"
    if re.match(pattern, string[0]):
        return True
    else:
        return False