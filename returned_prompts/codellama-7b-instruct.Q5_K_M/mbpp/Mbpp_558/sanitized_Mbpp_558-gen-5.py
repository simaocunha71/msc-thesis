def digit_distance_nums(num1,num2):
    sum = 0
    for i in range(max(len(str(num1)),len(str(num2)))):
        if i < len(str(num1)) and i < len(str(num2)):
            sum += abs(int(str(num1)[i]) - int(str(num2)[i]))
        elif i < len(str(num1)):
            sum += int(str(num1)[i])
        else:
            sum += int(str(num2)[i])
    return sum