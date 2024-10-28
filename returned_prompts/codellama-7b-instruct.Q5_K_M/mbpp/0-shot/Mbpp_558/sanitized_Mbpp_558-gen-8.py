def digit_distance_nums(num1, num2):
    sum = 0
    for i in str(abs(num1-num2)):
        sum += int(i)
    return sum