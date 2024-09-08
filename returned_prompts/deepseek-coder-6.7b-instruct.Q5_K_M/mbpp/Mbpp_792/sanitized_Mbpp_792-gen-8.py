def count_list(nested_list):
    count = 0
    for i in nested_list:
        if isinstance(i, list):
            count += 1
    return count