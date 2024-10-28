def remove_nested(tuple_):
    result = []
    for element in tuple_:
        if isinstance(element, tuple):
            result.extend(remove_nested(element))
        else:
            result.append(element)
    return tuple(result)