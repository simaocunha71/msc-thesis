def extract_values(s):
    return [i.strip('"').strip("'") for i in s.split(',')]
    # or using re
    # import re
    # return re.findall(r'"[^"]*"|\'[^\']\'', s)  # assuming single quotes are allowed