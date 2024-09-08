def count_list(lists):
    count = 0
    for l in lists:
        if type(l) == list:
            count += 1
    return count