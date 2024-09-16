def divisible_by_digits(startnum, endnum):
    numbers = []
    for i in range(startnum, endnum + 1):
        for j in range(9, 0, -1):
            if i % (j * 10 + j) == 0:
                numbers.append(i)
                break
    return numbers