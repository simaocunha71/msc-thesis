    sum = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 0 and i % 2 == 0:
            sum += lst[i]

    return sum


