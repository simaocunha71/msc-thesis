def count_Occurrence(t, lst):
    occurrence = {}
    for i in t:
        if i in lst:
            if i in occurrence:
                occurrence[i] += 1
            else:
                occurrence[i] = 1
    return sum(occurrence.values())