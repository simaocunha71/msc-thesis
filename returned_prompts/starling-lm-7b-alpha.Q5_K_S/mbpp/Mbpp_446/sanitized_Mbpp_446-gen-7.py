def count_Occurrence(tup,list_):
    count = 0
    for i in list_:
        if i in tup:
            count += tup.count(i)
    return count