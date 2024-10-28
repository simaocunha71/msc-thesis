def tup_string(tup):
    return ''.join(tup).replace(',', '').replace('(', '').replace(')', '').replace('\'', '').replace('"', '').replace(' ', '').lower()  # remove unwanted characters and convert to lowercase
    # or
    return ''.join(tup).replace(',', '').replace('(', '').replace(')', '').replace('\'', '').replace('"', '').replace(' ', '').lower().strip()  # remove unwanted characters and convert to lowercase and strip leading/trailing spaces