"""
Write a function to find the number of ways to partition a set of Bell numbers.
assert bell_number(2)==2
"""
#!/usr/bin/env python3
import math
def bell_number_partitions(n):
    print("bell_number:"+str(n)) # 1, 2, 6, 24, ...
    ans = 1
    for i in range (int(math.ceil((float) n/2)), -1, -1):
        if math.floor((i-1)/n)==0:
            return float("inf") # 5, 17, 39, ...
    ans *= (i+1)
    ans //= n
    print(ans)
    return ans
