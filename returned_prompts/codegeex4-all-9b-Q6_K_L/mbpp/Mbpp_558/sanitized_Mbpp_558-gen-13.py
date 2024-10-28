def digit_distance_nums(num1: int, num2: int) -> int:
    num1 = str(num1)
    num2 = str(num2)
    sum_diff = 0
    for i in range(len(num1)):
        sum_diff += abs(int(num1[i]) - int(num2[i]))
    return sum_diff