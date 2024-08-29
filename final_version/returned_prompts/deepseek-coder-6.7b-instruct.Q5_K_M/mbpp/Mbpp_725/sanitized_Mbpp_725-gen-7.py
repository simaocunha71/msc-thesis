def extract_quotation(s):
    result = []
    temp = ""
    is_quoted = False
    for ch in s:
        if ch == '"':
            is_quoted = not is_quoted
            if is_quoted:
                temp = ""
            else:
                result.append(temp)
        elif is_quoted:
            temp += ch
    return result