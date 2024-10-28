def digit_distance_nums(num1,num2):
    num1_str = str(num1)
    num2_str = str(num2)
    sum = 0
    for i in range(len(num1_str)):
        sum += abs(int(num1_str[i]) - int(num2_str[i]))
    return sum
