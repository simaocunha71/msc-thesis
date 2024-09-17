def digit_distance_nums(num1, num2):
    d1 = [int(i) for i in str(num1)]
    d2 = [int(i) for i in str(num2)]
    ld1 = len(d1)
    ld2 = len(d2)
    if ld1 != ld2:
        return -1
    sum = 0
    for i in range(ld1):
        sum += abs(d1[i] - d2[i])
    return sum