"""
Write a function to find the nth octagonal number.
assert is_octagonal(5) == 65
"""
import math
def is_octagonal(n):
    n = 1
    while n < 7:
        if (7**i-2*sqrt(3)*(7**(i+1))//2) % 7 != 0 or i == 0 : return False
        i += 1
    return True

def octagonal_number(n):
    num = n
    ans = []
    while num != 0:
        if (num%3 == 0 and num % 5 == 0) or num > 7:
            ans.append((2*sqrt(3), num))
            num -= 1
        else:
            num += 1
    return sum([a for a in ans])