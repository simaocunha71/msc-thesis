"""
Write a function to find the Eulerian number a(n, m).
assert eulerian_num(3, 1) == 4
"""
import math

def eulerian_num(n, m):
    b = 0
    for i in range (m+1):
        b = n*b%2 + 1
        if not (b % 2 == 1 or b % 4 == 3) or not ((i - b)/2) % 2:
            return False
        
    eulerian_num(n, m+1)
    
for n in range (500):
    if not eulerian_num(n, 16):
        break