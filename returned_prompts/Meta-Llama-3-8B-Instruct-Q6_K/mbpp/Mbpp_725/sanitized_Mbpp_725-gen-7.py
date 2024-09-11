def extract_quotation(s):
    result = []
    temp = ''
    for char in s:
        if char == '"':
            if temp:
                result.append(temp)
                temp = ''
        else:
            temp += char
    if temp:
        result.append(temp)
    return result