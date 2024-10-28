def count_integer(list):
    count = 0
    for i in list:
        if type(i) == int:
            count += 1
    return count