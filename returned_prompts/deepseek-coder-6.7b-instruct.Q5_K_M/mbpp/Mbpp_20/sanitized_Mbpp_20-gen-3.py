def is_woodall(n):
    if n < 10:
        return False
    else:
        str_n = str(n)
        sum_of_digits = sum(int(digit) for digit in str_n)
        return n % sum_of_digits == 0