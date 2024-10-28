    bin_number = bin(N).split('b')[1]
    sum_of_digits = sum([int(digit) for digit in bin_number])
    return sum_of_digits


