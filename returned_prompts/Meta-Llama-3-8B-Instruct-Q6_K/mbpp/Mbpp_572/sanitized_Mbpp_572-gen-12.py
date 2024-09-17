def two_unique_nums(list_of_lists):
    result = []
    for lst in list_of_lists:
        result.extend(list(set(lst)))
    return list(set(result))