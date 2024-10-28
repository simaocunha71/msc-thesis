
import re
def change_date_format(date_string):
    pattern = r"(\d{4})-(\d{2})-(\d{2})"
    replacement = r"\3-\2-\1"
    return re.sub(pattern, replacement, date_string)


