
import re
def check_str(test_str):
    return bool(re.match(r'^[aeiou]', test_str, re.I))


