def count_integer(l):
    count = 0
    for i in l:
        if isinstance(i, int):
            count += 1
    return count