def extract_values(s):
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