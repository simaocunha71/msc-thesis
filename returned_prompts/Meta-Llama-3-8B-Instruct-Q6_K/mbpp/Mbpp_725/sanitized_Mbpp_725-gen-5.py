def extract_quotation(s):
    result = []
    start = 0
    for i in range(len(s)):
        if s[i] == '"':
            if i > start:
                result.append(s[start:i])
            start = i + 1
    if start < len(s):
        result.append(s[start:])
    return result