def extract_values(s):
    values = []
    start = None
    for i, char in enumerate(s):
        if char == '"':
            if start is None:
                start = i
            elif start != i - 1:
                values.append(s[start+1:i])
                start = None
    return values