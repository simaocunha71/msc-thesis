def count_Occurrence(t,l):
    occ = 0
    for i in l:
        occ += t.count(i)
    return occ