def divisible_by_digits(startnum, endnum):
    result = []
    for num in range(startnum, endnum+1):
        divisors = set()
        for digit in str(num):
            if digit == '0':
                break
            if num % int(digit) == 0:
                divisors.add(int(digit))
        if len(divisors) == len(set(str(num))):
            result.append(num)
    return result