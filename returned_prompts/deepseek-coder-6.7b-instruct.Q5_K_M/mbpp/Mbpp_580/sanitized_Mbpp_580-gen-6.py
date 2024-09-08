def extract_even(tup):
    result = []
    for i in tup:
        if type(i) == tuple:
            result.append(extract_even(i))
        elif i % 2 == 0:
            result.append(i)
    return tuple(result)