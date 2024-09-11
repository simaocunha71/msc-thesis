def power_base_sum(base, power):
    result = 0
    while power > 0:
        result += base % 10
        base = base // 10
        power -= 1
    return result

# assert power_base_sum(2, 100) == 115

"""
Write a function that takes a number as input and returns its binary representation as a string.
assert binary(5) == '101'
"""

def binary(num):
    result = ''
    while num > 0:
        result += str(num % 2)
        num //= 2
    return result[::-1]

# assert binary(5) == '101'

"""
Write a function that takes a number as input and returns its decimal representation as a string.
assert decimal(11010110) == '133'
"""

def decimal(num):
    result = 0
    for i in range(len(num)):
        result += int(num[i]) * 2 ** (len(num) - i - 1)
    return str(result)

# assert decimal(11010110) == '133'

"""
Write a function that takes a number as input and returns its octal representation as a string.
assert octal(133) == '221'
"""

def octal(num):
    result = 0
    while num > 0:
        result += num % 8
        num //= 8
    return str(result)

# assert octal(133) == '221'

"""
Write a function that takes a number as input and returns its hexadecimal representation as a string.
assert hex(133) == '85'
"""

def hex(num):
    result = 0
    while num > 0:
        result += num % 16
        num //= 16
    return str(result)

# assert hex(133) == '85'

"""
Write a function that takes a number as input and returns the number of dig