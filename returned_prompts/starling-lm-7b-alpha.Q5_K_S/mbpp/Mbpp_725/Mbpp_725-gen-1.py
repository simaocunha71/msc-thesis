
import re
def extract_quotation(s):
    return re.findall(r'"(\w+)"', s)


