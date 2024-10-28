import re
def extract_quotation(str_data: str) -> list:
    return re.findall(r'"([^"]*)"', str_data)