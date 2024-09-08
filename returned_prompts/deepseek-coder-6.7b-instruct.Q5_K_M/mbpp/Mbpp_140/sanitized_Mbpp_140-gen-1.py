def extract_singly(lst):
    result = []
    for sublist in lst:
        if isinstance(sublist, tuple):
            result.extend(sublist)
        else:
            result.append(sublist)
    return set(result)