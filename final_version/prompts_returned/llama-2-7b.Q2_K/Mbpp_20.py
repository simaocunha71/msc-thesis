"""
Write a function to check if the given number is woodball or not.
assert is_woodall(383) == True
"""
import math

def is_woodall(n):
    l = list(range(1, n))
    l.remove(l[-1]) # remove last element
    s = "".join([str(i) for i in l])
    a = int(''.join([str(2 * (x + x + 1)) for x in s]))
    b = str(n-a-3)
    c = b[::-1] # reverse the string to get the answer backward
    d = int("0".join(c))
    if d == a:
        return True
    else:
        return False

print("is_woodall(420) is ", is_woodall(420)) # True, because 420=13!+1
# print('is_woodall(9) is ', is_woodall(9))    # True
