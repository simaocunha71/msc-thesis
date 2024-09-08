def count_integer(lst):
    count = 0
    for item in lst:
        if type(item) == int:
            count += 1
    return count