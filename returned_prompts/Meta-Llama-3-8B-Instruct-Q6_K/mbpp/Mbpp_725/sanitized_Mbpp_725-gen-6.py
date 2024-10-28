def extract_quotation(s):
    result = []
    current = ''
    in_quotes = False
    for char in s:
        if char == '"':
            if in_quotes:
                result.append(current)
                current = ''
                in_quotes = False
            else:
                in_quotes = True
        else:
            if in_quotes:
                current += char
    return result