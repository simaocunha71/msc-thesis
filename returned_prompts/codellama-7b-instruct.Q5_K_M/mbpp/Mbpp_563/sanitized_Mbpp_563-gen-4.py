import re
def extract_values(str):
    return re.findall(r'"([^"]*)"', str)