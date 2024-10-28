    sum = 0
    for i, element in enumerate(lst):
        if i % 3 == 0:
            sum += element ** 3
        elif i % 4 == 0:
            sum += element ** 2
    return sum


