"""
The smallest triangular number with n digits has the form 10^(n-1) + k, where k is a positive integer.
The index of this triangular number is k.
So, we need to find the smallest k such that 10^(n-1) + k is a triangular number.
We can use the formula for the nth triangular number t_n = n*(n+1)/2 to solve this.
"""

def find_Index(n):
    i = 1
    while True:
        t = i*(i+1)//2
        if 10**(n-1) <= t < 10**n:
            return i
        i += 1

print(find_Index(2))  # 4




