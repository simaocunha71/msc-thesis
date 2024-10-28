def count_Occurrence(tup, list_):
    count = 0
    for i in list_:
        count += tup.count(i)
    return count