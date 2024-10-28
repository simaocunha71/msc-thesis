def count_Occurrence(tup, lst):
    count_dict = {}
    for elem in lst:
        count_dict[elem] = tup.count(elem)
    return count_dict