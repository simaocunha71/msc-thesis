def extract_values(s):
    values = []
    start = False
    current_value = ''
    for char in s:
        if char == '"':
            if start:
                values.append(current_value)
                current_value = ''
                start = False
            else:
                start = True
        elif start:
            current_value += char
    return values