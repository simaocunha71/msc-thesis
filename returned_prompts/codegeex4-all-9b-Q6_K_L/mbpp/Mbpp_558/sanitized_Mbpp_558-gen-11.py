def digit_distance_nums(num1: int, num2: int) -> int:
    num1 = str(num1)
    num2 = str(num2)
    diff_sum = 0
    if len(num1) > len(num2):
        num2 = num2.zfill(len(num1))
    else:
        num1 = num1.zfill(len(num2))
    for i in range(len(num1)):
        diff_sum += abs(int(num1[i]) - int(num2[i]))
    return diff_sum