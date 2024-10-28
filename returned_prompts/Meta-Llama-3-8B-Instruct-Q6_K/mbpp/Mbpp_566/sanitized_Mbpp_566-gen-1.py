def sum_digits(n):
    return sum(int(digit) for digit in str(n))  # convert to string, iterate over each char, convert back to int and sum