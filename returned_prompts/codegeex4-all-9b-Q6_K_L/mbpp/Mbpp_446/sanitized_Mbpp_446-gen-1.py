def count_Occurrence(tup, lst):
    count = 0
    for ele in lst:
        count += tup.count(ele)
    return count