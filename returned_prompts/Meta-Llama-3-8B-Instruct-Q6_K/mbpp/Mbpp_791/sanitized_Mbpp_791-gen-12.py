def remove_nested(t):
    result = []
    for x in t:
        if isinstance(x, tuple):
            result.extend(remove_nested(x))
        else:
            result.append(x)
    return tuple(result)