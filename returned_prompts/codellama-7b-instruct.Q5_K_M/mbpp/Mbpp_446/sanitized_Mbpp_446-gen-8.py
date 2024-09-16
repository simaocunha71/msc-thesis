def count_Occurrence(list, tuple):
    count = 0
    for i in tuple:
        count += list.count(i)
    return count