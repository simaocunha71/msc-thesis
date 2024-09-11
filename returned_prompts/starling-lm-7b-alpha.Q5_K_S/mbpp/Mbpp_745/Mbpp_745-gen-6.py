from math import sqrt


def is_divisible_by_digits(n):
    if n == 0:
        return False
    if n % int(str(n)[0]) == 0:
        return True
    else:
        return is_divisible_by_digits(n % int(str(n)[0]))


def divisible_by_digits(startnum, endnum):
    if startnum == endnum:
        return [startnum] if is_divisible_by_digits(startnum) else []
    if startnum > endnum:
        return []
    if startnum % int(str(startnum)[0]) == 0:
        if endnum % int(str(endnum)[0]) != 0:
            return [startnum] + divisible_by_digits(startnum + 1, endnum)
        else:
            return [startnum] + divisible_by_digits(startnum + 1, endnum) + divisible_by_digits(startnum + 1, endnum)
    else:
        return divisible_by_digits(startnum + 1, endnum)


# assert divisible_by_digits(1,22)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
# assert divisible_by_digits(3, 22)==[3, 4, 6, 8, 9, 12, 15, 18, 22]
# assert divisible_by_digits(10, 22)==[10, 12, 15, 22]

divisible_by_digits(1, 22)

# AssertionError: divisible_by_digits(1, 22) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

"""
def divisible