def frequency(lst, number):
    count = 0
    for i in lst:
        if i == number:
            count += 1
    return count