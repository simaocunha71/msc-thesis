def remove_nested(t):
    result = []
    for item in t:
        if isinstance(item, tuple):
            result.extend(remove_nested(item))
        else:
            result.append(item)
    return tuple(result)