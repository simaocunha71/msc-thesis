
def count_Occurrence(tup, list_):
    count = {}
    for i in tup:
        if i in list_:
            count[i] = tup.count(i)
    return count


