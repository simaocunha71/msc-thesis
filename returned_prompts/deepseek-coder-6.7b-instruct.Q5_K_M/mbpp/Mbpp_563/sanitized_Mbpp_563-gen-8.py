def extract_values(s):
    values = []
    current_value = ""
    in_quote = False
    for char in s:
        if char == '"':
            in_quote = not in_quote
        elif char == ',' and not in_quote:
            values.append(current_value.strip())
            current_value = ""
        else:
            current_value += char
    values.append(current_value.strip())
    return values