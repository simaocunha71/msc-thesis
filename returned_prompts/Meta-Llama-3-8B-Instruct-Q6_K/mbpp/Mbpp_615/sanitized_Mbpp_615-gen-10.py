def average_tuple(t):
    result = []
    for i in t:
        avg = sum(i) / len(i)
        result.append(avg)
    return result