def divisible_by_digits(startnum, endnum):
    numbers = []
    for num in range(startnum, endnum + 1):
        if all(num % int(i) == 0 for i in str(num) if i != '0'):
            numbers.append(num)
    return numbers