def digit_distance_nums(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    diff_sum = 0
    for i in range(len(num1)):
        diff_sum += abs(int(num1[i]) - int(num2[i]))
    return diff_sum