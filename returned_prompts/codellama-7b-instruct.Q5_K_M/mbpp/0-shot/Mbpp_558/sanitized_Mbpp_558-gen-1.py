def digit_distance_nums(num1, num2):
    num1_list = [int(i) for i in str(num1)]
    num2_list = [int(i) for i in str(num2)]
    result = 0
    for i in range(len(num1_list)):
        result += abs(num1_list[i]-num2_list[i])
    return result