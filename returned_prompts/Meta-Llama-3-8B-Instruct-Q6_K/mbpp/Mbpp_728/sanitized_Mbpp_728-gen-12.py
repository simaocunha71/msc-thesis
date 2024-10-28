def sum_list(a, b):
    result = []
    for x, y in zip(a, b):
        result.append(x+y)
    return result