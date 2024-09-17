import re
def check_str(string: str) -> bool:
    pattern = r'^[aeiouAEIOU]'
    return bool(re.match(pattern, string))