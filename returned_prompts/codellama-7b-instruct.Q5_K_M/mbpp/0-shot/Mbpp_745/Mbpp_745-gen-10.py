def divisible_by_digits(startnum, endnum):
    numlist = []
    for i in range(startnum, endnum+1):
        if is_divisible_by_digits(i):
            numlist.append(i)
    return numlist

def is_divisible_by_digits(num):
    for digit in str(num):
        if num % int(digit) != 0:
            return False
    return True


