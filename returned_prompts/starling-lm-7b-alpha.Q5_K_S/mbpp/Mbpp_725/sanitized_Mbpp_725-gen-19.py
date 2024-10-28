def extract_quotation(s: str) -> list:
    result = []
    start = False
    for i, c in enumerate(s):
        if c == '"':
            start = not start
        elif start:
            result.append(s[i])
    return result