def digit_distance_nums(num1, num2):
    max_num = max(num1, num2)
    min_num = min(num1, num2)
    digit_distance = 0
    while max_num > 0 or min_num > 0:
        max_digit = max_num % 10 if max_num > 0 else 0
        min_digit = min_num % 10 if min_num > 0 else 0
        digit_distance += abs(max_digit - min_digit)
        max_num //= 10
        min_num //= 10
    return digit_distance