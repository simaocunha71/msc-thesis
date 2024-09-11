def remove_nested(tup):
    new_tup = []
    for item in tup:
        if type(item) == tuple:
            new_tup.extend(remove_nested(item))
        else:
            new_tup.append(item)
    return tuple(new_tup) if new_tup else ()  # Convert list back to tuple and return it. If the list is empty, return an empty tuple.