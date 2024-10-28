```
def highest_Power_of_2(n):
    power = 0
    while 2 ** power <= n:
        power += 1
    return 2 ** (power - 1)
```
This function works by starting with the smallest power of 2 (2^0 = 1) and continually increasing the power until 2^power is greater than n. At that point, it returns 2^(power-1), which is the highest power of 2 that is less than or equal to n.

The unit test `assert highest_Power_of_2(10) == 8` ensures that the function is working correctly. In this case, the highest power of 2 less than or equal to 10 is indeed 8 (2^3). The function correctly returns 8 in this case. 