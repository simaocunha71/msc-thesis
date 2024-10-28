def count_Occurrence(tup, list):
    count = 0
    for i in list:
        count += tup.count(i)
    return count