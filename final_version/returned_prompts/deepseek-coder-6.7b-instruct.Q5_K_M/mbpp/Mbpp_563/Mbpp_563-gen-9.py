def extract_values(s):
    import re
    return re.findall('"([^"]*)"', s)

assert extract_values('"Python",  "PHP",  "Java"')==['Python', 'PHP', 'Java']


# 2.
