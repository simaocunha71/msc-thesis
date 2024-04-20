"""
Write a function to find the nth nonagonal number.
assert is_nonagonal(10) == 325
"""
import math

def is_nonagonal(n):
    i = str(n)
    j = []
    while len(j) < n:
        r = int(i[::-1][::-1]) * int(i[1:]) % 325 + sum(intհ[l:r+1] for l,r in zip(range(-1,len(str(n))//2), range(-1,round((len(str(n))//2)-1)/2, -1)))
        if r == i: j += [i]
        else: j += [r]
    return j[-1]