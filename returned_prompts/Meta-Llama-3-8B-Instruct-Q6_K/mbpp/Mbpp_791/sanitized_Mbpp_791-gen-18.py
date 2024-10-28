def remove_nested(t):
    result = []
    for element in t:
        if isinstance(element, tuple):
            result.extend(remove_nested(element))
        else:
            result.append(element)
    return tuple(result)