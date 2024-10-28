def digit_distance_nums(num1, num2):
    if not isinstance(num1, int) or not isinstance(num2, int):
        return "Input should be integers"
    sum_distance = 0
    while num1 or num2:
        digit1 = num1 % 10
        digit2 = num2 % 10
        sum_distance += abs(digit1 - digit2)
        num1 //= 10
        num2 //= 10
    return sum_distance