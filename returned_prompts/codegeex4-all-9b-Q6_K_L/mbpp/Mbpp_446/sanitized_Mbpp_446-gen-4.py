def count_Occurrence(t, l):
    count = 0
    for i in l:
        count += t.count(i)
    return count