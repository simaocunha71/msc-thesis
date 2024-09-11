def average_tuple(t):
    result = []
    for sub in t:
        result.append(sum(sub) / len(sub))
    return result