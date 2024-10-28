def remove_nested(tup):
    result = []
    for elem in tup:
        if isinstance(elem, tuple):
            result.extend(remove_nested(elem))
        else:
            result.append(elem)
    return tuple(result) if result else ()  # Convert to tuple and remove empty tuples