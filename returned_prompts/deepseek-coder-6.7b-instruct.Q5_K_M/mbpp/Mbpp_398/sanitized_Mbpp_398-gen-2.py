def sum_of_digits(lst):
    result = []
    for num in lst:
        sum_digits = 0
        while num > 0:
            digit = num % 10
            sum_digits += digit
            num = num // 10
        result.append(sum_digits)
    return result