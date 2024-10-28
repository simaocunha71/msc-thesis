def extract_singly(lst):
    result = set()
    for item in lst:
        if isinstance(item, list):
            result.update(extract_singly(item))
        else:
            result.add(item)
    return result