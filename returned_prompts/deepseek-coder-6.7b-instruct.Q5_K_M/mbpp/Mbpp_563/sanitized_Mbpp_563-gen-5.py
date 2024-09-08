def extract_values(s):
    import re
    matches = re.findall(r'"([^"]*)"', s)
    return matches