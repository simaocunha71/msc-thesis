def digit_distance_nums(num1, num2):
    sum = 0
    for i in range(max(len(str(num1)), len(str(num2)))):
        if i < len(str(num1)):
            sum += abs(int(str(num1)[i]) - int(str(num2)[i]))
        else:
            sum += abs(int(str(num2)[i]) - int(str(num1)[i]))
    return sum
