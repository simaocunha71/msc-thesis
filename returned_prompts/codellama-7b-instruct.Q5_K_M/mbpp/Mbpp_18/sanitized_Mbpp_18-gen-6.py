import re
def remove_dirty_chars(first_string, second_string):
    return re.sub(f"[{second_string}]", "", first_string)