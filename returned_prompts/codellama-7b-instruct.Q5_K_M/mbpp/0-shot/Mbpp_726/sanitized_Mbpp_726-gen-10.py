def multiply_elements(tup):
    new_tup = []
    for i in range(len(tup) - 1):
        new_tup.append(tup[i] * tup[i + 1])
    return tuple(new_tup)