def extract_singly(nested_list):
    result = set()
    for lst in nested_list:
        result.update(lst)
    return result