import re
def extract_values(string):
    pattern = re.compile(r'"([^"]*)"')
    matches = pattern.findall(string)
    return matches