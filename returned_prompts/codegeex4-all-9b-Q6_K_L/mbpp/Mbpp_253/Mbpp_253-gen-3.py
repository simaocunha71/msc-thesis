def count_integer(lst):
    count = 0
    for i in lst:
        if type(i) == int:
            count += 1
    return count

