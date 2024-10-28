def count_Occurrence(tup, lst):
    count = 0
    for i in tup:
        if i in lst:
            count += tup.count(i)
    return count