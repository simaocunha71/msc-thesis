import re
def extract_values(s):
    s = s.replace('"', '')
    return s.split(', ')