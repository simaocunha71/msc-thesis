def count_list(lists):
    count = 0
    for l in lists:
        if isinstance(l, list):
            count += 1
    return count