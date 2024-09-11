"""
def sum_digits(num):
    summ = 0
    while num:
        summ += num%10
        num //= 10
    return summ
"""

def sum_digits(num):
    summ = 0
    while num:
        summ += num % 10
        num //= 10
    return summ

assert sum_digits(345)==12

def sum_digits(num):
    if num==0:
        return 0
    else:
        return num%10 + sum_digits(num//10)

assert sum_digits(345)==12

def sum_digits(num):
    if num==0:
        return 0
    return num%10 + sum_digits(num//10)

assert sum_digits(345)==12

def sum_digits(num):
    if num==0:
        return 0
    else:
        return num%10 + sum_digits(num//10)

assert sum_digits(345)==12

def sum_digits(num):
    if num==0:
        return 0
    else:
        return num%10 + sum_digits(num//10)

assert sum_digits(345)==12

def sum_digits(num):
    if num==0:
        return 0
    else:
        return num%10 + sum_digits(num//10)

assert sum_digits(345)==12

def sum_digits(num):
    if num==0:
        return 0
    else:
        return num%10 + sum_digits(num//10)

assert sum_digits(345)==12

def sum_digits(num):
    if num==0:
        return 0
    else:
        return num%10 + sum_digits(num//10)

assert sum_digits(345)