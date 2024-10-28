def drop_empty(dictionary):
    result = {}
    for key, value in dictionary.items():
        if value is not None:
            result[key] = value
    return result