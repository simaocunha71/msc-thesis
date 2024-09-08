def digit_distance_nums(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    sum = 0
    for i in range(min(len(num1), len(num2))):
        sum += abs(int(num1[i]) - int(num2[i]))
    return sum

print(digit_distance_nums(1,2))




