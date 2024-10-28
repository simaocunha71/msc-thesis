
def rounded_avg(n, m):
    if n > m:
        return -1
    else:
        avg = (n + m) / 2
        avg = round(avg)
        return bin(avg).replace("0b", "")

print(rounded_avg(1, 5))  # => "0b11"
print(rounded_avg(7, 5))  # => -1
print(rounded_avg(10, 20))  # => "0b1111"
print(rounded_avg(20, 33))  # => "0b11010"


# 1. Check if n is greater than m. If it is, return -1.
# 2. If not, compute the average of n and m. Round this average to the nearest integer.
# 3. Convert this rounded average to binary and return it.
# 4. Remove the "0b" at the start of the binary number and return the rest of the number.

"""
def rounded_avg(n, m):
    if n > m:
        return -1
    avg = round((n + m) / 2)
    return bin(avg).replace("0b", "")
"""

"""
def rounded_avg(n, m):
    if n > m:
        return -1
    else:
        avg = (n + m) / 2.0
        avg = round(avg)
        return bin(avg).replace('0b', '')
"""

"""
def rounded_avg(n, m):
    if n > m:
        return -1
    else:
        return bin(round((n + m) / 2))[2:]
"""

"""
def rounded_avg(n, m):
    return -1 if n > m else bin(round((n + m) / 2))[2:]
"""
"""
def rounded_avg(n, m):
    return bin(round((n + m) / 2))[2:] if n <= m else -1
"""