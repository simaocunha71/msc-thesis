def extract_quotation(s):
    result = []
    temp = ''
    in_quote = False
    for char in s:
        if char == '"':
            in_quote = not in_quote
        elif in_quote:
            temp += char
        else:
            if temp:
                result.append(temp)
                temp = ''
    return result