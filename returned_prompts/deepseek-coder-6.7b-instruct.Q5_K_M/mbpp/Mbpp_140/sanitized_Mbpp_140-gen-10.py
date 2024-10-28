def extract_singly(list_of_lists):
    result = []
    for sublist in list_of_lists:
        if isinstance(sublist, tuple):
            result.extend(sublist)
        else:
            result.append(sublist)
    return set(result)