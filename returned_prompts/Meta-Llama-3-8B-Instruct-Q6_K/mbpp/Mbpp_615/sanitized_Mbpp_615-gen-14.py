def average_tuple(t):
    result = []
    for i in t:
        result.append(sum(i) / len(i))
    return result