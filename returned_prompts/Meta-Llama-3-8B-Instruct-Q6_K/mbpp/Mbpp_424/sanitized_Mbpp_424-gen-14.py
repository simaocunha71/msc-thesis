def extract_rear(t):
    result = []
    for s in t:
        if s:
            result.append(s[-1])
    return result