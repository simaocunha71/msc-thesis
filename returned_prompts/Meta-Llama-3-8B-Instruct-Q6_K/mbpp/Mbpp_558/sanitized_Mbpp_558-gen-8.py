def digit_distance_nums(num1, num2):
    total_distance = 0
    for i in range(max(len(str(num1)), len(str(num2)))):
        digit1 = str(num1)[i] if i < len(str(num1)) else '0'
        digit2 = str(num2)[i] if i < len(str(num2)) else '0'
        total_distance += abs(int(digit1) - int(digit2))
    return total_distance