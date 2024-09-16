def merge_dictionaries_three(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result