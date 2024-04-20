"""
Write a python function to find the smallest power of 2 greater than or equal to n.
assert next_power_of_2(0) == 1
"""

def next_power_of_2(n):
    if not isinstance(n, int) or n < 0:
        raise Exception("Invalid type")
        
    res = n
    
    if res > 0 and res & (res - 1) == 0:
        return 1
        
    while True:
        while next_power_of_2(n*2) < n:
            res *= 2
            
        return res
