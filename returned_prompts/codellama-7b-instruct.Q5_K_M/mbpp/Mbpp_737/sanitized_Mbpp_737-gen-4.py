import re
def check_str(my_str):
    if re.match(r"^[aeiouAEIOU]", my_str):
        return True
    else:
        return False