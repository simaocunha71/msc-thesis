def count_Occurrence(tuple,list):
    count = 0
    for i in tuple:
        if i in list:
            count += 1
    return count