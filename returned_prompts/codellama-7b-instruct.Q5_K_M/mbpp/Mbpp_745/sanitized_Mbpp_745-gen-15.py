def divisible_by_digits(startnum: int, endnum: int):
    divisible_nums = []
    for i in range(startnum, endnum+1):
        if i == 0:
            continue
        for j in range(9, 0, -1):
            if i % (j+1) == 0:
                divisible_nums.append(i)
                break
    return divisible_nums