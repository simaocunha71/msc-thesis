def is_Diff(num):
    str_num = str(num)
    sum_of_digits = sum(int(digit) for digit in str_num)
    sum_of_digits_reversed = sum(int(digit) for digit in reversed(str_num))
    return (sum_of_digits - sum_of_digits_reversed) % 11 == 0