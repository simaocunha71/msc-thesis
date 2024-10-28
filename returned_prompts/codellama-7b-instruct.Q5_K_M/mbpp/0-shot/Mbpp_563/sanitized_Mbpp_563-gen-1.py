def extract_values(string):
    values = []
    for value in string.split(','):
        value = value.strip().strip('"')
        values.append(value)
    return values