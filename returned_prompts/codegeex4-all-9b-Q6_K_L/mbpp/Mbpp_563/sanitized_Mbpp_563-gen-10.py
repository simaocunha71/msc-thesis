def extract_values(s):
    result = []
    start = False
    temp = ""
    for i in s:
        if i == '"':
            start = not start
            if start:
                continue
            result.append(temp)
            temp = ""
        elif start:
            temp += i
    return result