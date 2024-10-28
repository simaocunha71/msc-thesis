def divisible_by_digits(startnum, endnum):
    result = []
    for i in range(startnum, endnum+1):
        if is_divisible(i, list(str(i))):
            result.append(i)
    return result

def is_divisible(num, digits):
    for digit in digits:
        if num % int(digit) != 0:
            return False
    return True

print(divisible_by_digits(1,22))
print(divisible_by_digits(1,23))
print(divisible_by_digits(10,22))
print(divisible_by_digits(10,23))



