def digit_distance_nums(num1, num2):
    sum = 0
    while num1 > 0 or num2 > 0:
        digit1 = num1 % 10
        digit2 = num2 % 10
        sum += abs(digit1 - digit2)
        num1 //= 10
        num2 //= 10
    return sum