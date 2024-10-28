import re
def extract_values(string):
    return re.findall(r'"(\w+)"', string)