    sum = 0
    for idx, value in enumerate(lst):
        if idx % 3 == 0:
            sum += value ** 2
        elif idx % 4 == 0:
            sum += value ** 3
        else:
            sum += value
    return sum

