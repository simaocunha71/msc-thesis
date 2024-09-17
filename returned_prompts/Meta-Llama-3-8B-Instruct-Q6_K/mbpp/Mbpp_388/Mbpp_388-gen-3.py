```
def highest_Power_of_2(n):
    power = 0
    while 2 ** power <= n:
        power += 1
    return 2 ** (power - 1)
```





The problem asks you to write a function that finds the highest power of 2 that is less than or equal to a given number `n`. 

The unit test `assert highest_Power_of_2(10) == 8` helps in understanding the problem better. It means that the highest power of 2 that is less than or equal to 10 is 8.

To solve this problem, we can start from the smallest power of 2 (2^0 = 1) and keep increasing the power until the power of 2 is greater than `n`. The last power of 2 that is less than or equal to `n` is the highest power of 2 that we are looking for. 

Here is the Python function that solves the problem:

```
def highest_Power_of_2(n):
    power = 0
    while 2 ** power <= n:
        power += 1
    return 2 ** (power - 1)
```

This function works by initializing a variable `power` to 0. Then it enters a loop where it keeps increasing `power` until the power of 2 is greater than `n`. The last power of 2 that is less than or equal to `n` is `2 ** (power - 1)`, so the function returns this value. 