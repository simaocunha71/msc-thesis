def extract_values(s):
    result = []
    start = None
    for i, c in enumerate(s):
        if c == '"':
            if start is None:
                start = i
            elif i > start + 1:
                result.append(s[start+1:i])
                start = None
    return result