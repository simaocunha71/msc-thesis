def digit_distance_nums(num1, num2):
    diff = abs(num1 - num2)
    sum = 0
    while diff > 0:
        sum += diff % 10
        diff //= 10
    return sum