def divisible_by_digits(startnum, endnum):
    divisible_numbers = []
    for i in range(startnum, endnum+1):
        digits = [int(digit) for digit in str(i)]
        if all(i % digit == 0 for digit in digits):
            divisible_numbers.append(i)
    return divisible_numbers