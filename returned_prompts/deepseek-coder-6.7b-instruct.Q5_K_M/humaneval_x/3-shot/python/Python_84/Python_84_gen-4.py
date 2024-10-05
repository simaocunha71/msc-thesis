    binary_string = bin(N)[2:]
    sum_of_digits = 0
    for digit in binary_string:
        sum_of_digits += int(digit)
    return bin(sum_of_digits)[2:]

