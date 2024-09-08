def remove_nested(tup):
    result = []
    for i in tup:
        if type(i) != tuple:
            result.append(i)
    return tuple(result)