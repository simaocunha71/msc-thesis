def divisible_by_digits(startnum, endnum):
    result = []
    for num in range(startnum, endnum+1):
        digits = [int(i) for i in str(num)]
        if all(num % digit == 0 for digit in digits):
            result.append(num)
    return result