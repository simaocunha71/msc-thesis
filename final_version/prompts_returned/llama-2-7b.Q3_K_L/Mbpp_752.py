"""
Write a function to find the nth jacobsthal number.  0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341, 683, 1365, 2731, ...
assert jacobsthal_num(5) == 11
"""
import math

def jacobsthal_num(n):
    k = 0
    for i in range (1, n+1):
        j = i - int(i/2)
        k += pow(j, j-1)/pow(2*j + 3, 2*k + 1)
    return k

if __name__ == "__main__":
   print (jacobsthal_num(5))