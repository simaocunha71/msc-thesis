def count_Occurrence(tup, lst):
    count = 0
    for i in lst:
        count += lst.count(i)
    return count