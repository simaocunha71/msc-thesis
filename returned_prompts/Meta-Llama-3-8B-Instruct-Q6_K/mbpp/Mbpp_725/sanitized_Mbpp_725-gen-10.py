def extract_quotation(s: str) -> list:
    result = []
    temp = ''
    for char in s:
        if char == '"':
            if temp:
                result.append(temp)
                temp = ''
        else:
            temp += char
    return result