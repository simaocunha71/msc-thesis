def digit_distance_nums(num1, num2):
    sum_diff = 0
    num1_str = str(num1)
    num2_str = str(num2)
    for i in range(min(len(num1_str), len(num2_str))):
        sum_diff += abs(int(num1_str[i]) - int(num2_str[i]))
    return sum_diff