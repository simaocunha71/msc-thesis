def extract_singly(lst):
    result = set()
    for sublist in lst:
        result.update(sublist)
    return result