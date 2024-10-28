def remove_nested(tup):
    result = []
    for item in tup:
        if isinstance(item, tuple):
            result.extend(remove_nested(item))
        else:
            result.append(item)
    return tuple(result)

#
