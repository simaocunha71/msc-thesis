def count_Occurrence(tup, lst):
    count = {}
    for i in tup:
        if i in lst:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
    return sum(count.values())