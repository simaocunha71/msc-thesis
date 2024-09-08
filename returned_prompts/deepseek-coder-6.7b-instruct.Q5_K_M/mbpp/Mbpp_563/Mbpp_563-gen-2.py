def extract_values(s):
    import re
    return re.findall(r'"([^"]*)"', s)

print(extract_values('"Python",  "PHP",  "Java"'))


