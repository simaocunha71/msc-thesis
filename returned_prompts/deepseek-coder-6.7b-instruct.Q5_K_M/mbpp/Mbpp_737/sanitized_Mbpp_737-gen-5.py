import re
def check_str(word):
    if re.match(r'^[aeiou]', word):
        return True
    else:
        return False