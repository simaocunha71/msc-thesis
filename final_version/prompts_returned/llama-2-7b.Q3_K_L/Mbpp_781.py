"""
Write a python function to check whether the count of divisors is even. 
assert count_divisors(10)
"""

def count_divisors(n):
    divisors = {}

    for i in range(2, n+1):
        if n % i == 0:
            divisor = True
            while i not in divisors.keys():
                divisors[i] = divisors.get(i-1, 0) + 1 if i > 1 else divisors[i]
        
    return divisors.get(n, 0) % 2 == 0
            