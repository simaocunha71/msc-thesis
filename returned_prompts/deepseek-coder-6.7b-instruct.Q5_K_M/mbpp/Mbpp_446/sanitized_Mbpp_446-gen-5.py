def count_Occurrence(tuple_in, list_in):
    count = 0
    for i in list_in:
        count += tuple_in.count(i)
    return count