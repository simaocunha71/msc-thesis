def count_list(lists):
    count = 0
    for item in lists:
        if isinstance(item, list):
            count += 1
    return count