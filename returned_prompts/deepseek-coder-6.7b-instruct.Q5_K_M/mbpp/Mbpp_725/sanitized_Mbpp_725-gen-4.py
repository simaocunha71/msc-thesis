def extract_quotation(s):
    import re
    return re.findall(r'"([^"]*)"', s)