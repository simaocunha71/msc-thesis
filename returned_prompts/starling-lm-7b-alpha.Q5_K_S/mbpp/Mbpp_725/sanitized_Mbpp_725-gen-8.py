import re
def extract_quotation(s):
    pattern = r'"(.*?)"'
    return re.findall(pattern, s)