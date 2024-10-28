import re
def extract_quotation(string: str) -> list:
    return re.findall(r'"([^"]*)"', string)