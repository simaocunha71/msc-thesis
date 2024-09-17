def digit_distance_nums(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1
    diff = 0
    while num2 > 0:
        diff += abs(num1 % 10 - num2 % 10)
        num1 //= 10
        num2 //= 10
    return diff