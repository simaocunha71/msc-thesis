def remove_nested(t):
    result = ()
    for element in t:
        if isinstance(element, tuple):
            result += remove_nested(element)
        else:
            result += (element,)
    return result