    sum = 0
    if lst == []:
        return 0
    else:
        for i in lst:
            if i % 2 != 0 and i >= 0 and i % 1 == 0:
                sum = sum + i * i
        return sum


