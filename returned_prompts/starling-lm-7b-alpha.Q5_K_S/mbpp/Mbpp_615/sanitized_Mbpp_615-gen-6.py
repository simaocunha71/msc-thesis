def average_tuple(t):
    result = []
    for tup in t:
        sum = 0
        for num in tup:
            sum += num
        result.append(sum / len(tup))
    return result