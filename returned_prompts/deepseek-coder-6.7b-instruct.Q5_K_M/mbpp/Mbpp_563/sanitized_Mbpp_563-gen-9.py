def extract_values(s):
    import re
    return re.findall('"([^"]*)"', s)