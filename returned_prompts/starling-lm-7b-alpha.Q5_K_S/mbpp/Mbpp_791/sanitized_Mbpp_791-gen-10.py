def remove_nested(t):
    result = []
    for elem in t:
        if type(elem) == tuple:
            result.append(remove_nested(elem))
        else:
            result.append(elem)
    return tuple(result)