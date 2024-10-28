```
def highest_Power_of_2(n):
    power = 0
    while 2**power <= n:
        power += 1
    return 2**(power-1)
```
This function starts with a power of 2 equal to 0, and then keeps increasing the power until 2 to the power of that number is greater than n. It then returns the power of 2 that is one less than this value. For example, if n is 10, the function will return 8, which is the highest power of 2 less than or equal to 10.