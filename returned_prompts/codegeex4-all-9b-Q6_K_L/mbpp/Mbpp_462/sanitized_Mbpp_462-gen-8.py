def combinations_list(lst):
    result = [[]]
    for item in lst:
        result.extend([combo + [item] for combo in result])
    return result