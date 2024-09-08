def extract_values(s):
    result = []
    start = False
    temp = ''
    for c in s:
        if c == '"':
            if start:
                result.append(temp)
                temp = ''
            start = not start
        elif start:
            temp += c
    return result