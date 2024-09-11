def sum_digits(n):
    return sum(int(digit) for digit in str(n))  # convert int to str and iterate over each character, convert back to int and sum them up.  # return sum