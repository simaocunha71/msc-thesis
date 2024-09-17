def concatenate_tuple(tup, delimiter):
    result = ""
    for elem in tup:
        result += str(elem) + delimiter
    return result[:-1]