def merge_dictionaries_three(*args):
    result = {}
    for dictionary in args:
        result.update(dictionary)
    return result

