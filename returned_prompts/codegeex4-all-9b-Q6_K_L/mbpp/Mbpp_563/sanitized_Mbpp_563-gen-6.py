import re
def extract_values(s):
    pattern = r'"([^"]*)"'
    return re.findall(pattern, s)