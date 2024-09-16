import re

def extract_values(str):
    return re.findall(r'"([^"]*)"', str)

extract_values('"Python", "PHP", "Java"')

