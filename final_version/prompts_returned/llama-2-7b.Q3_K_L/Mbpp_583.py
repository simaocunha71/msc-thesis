"""
Write a function which returns nth catalan number.
assert catalan_number(10)==16796
"""

def catalan_number(n):
    # write your code here
 
    if n == 0 or n == 1: 
        return 1
 
    elif n % 2 != 0 and n > 2:
        return n - 2 * (catalan_number(int((n-1) / 2))) + catalan_number(int((n-1) / 2))
  
    else:
        return 1

 