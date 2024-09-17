def find_Max_Num(digits):
    sorted_digits = sorted(str(digit) for digit in digits)
    max_num = ''
    for digit in sorted_digits:
        max_num += digit
    return int(max_num)