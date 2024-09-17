def extract_singly(lists):
    result = set()
    for lst in lists:
        result.update(lst)
    return result