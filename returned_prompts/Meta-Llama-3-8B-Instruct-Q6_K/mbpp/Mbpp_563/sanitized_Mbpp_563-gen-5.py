def extract_values(s):
    values = []
    start = 0
    for i in range(len(s)):
        if s[i] == '"':
            if i > start:
                values.append(s[start:i])
            start = i + 1
    return values[1:-1] if start < len(s) else values