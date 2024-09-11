def count_list(l):
    cnt = 0
    for i in l:
        if isinstance(i, list):
            cnt += 1
    return cnt