def digit_distance_nums(num1, num2):
    return sum(abs(int(digit) - int(digit2)) for digit, digit2 in zip(str(num1), str(num2))) if len(str(num1)) == len(str(num2)) else -1