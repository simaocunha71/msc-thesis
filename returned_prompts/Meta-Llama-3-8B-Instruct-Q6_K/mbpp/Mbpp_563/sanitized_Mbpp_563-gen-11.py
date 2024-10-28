import re
def extract_values(s):
    if s is None or s == '':
        return []
    return re.findall(r'"([^"]*)"', s)