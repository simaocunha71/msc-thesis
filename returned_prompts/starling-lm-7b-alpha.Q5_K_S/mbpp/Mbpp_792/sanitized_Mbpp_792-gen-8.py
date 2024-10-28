def count_list(l):
    count = 0
    for i in l:
        if isinstance(i, list):
            count += 1
    return count