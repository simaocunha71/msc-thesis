import re

def extract_values(string):
    matches = re.findall(r'"(.*?)"', string)
    return matches
