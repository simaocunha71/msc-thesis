def count_Occurrence(t, l):
    count = 0
    for item in t:
        if item in l:
            count += 1
    return count