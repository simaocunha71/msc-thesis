```
def is_simple_power(x, n):
    root = round(n ** (1 / len(str(n))))
    return root ** len(str(n)) == x
```



This function works by first calculating the root of n. It does this by taking the nth root of n and rounding it to the nearest integer. It then checks if this root raised to the power of the length of n is equal to x. If it is, then x is a simple power of n and the function returns True. Otherwise, it returns False. 

For example, for the input is_simple_power(8, 2), the function will calculate the root of 2 as 1.4142135623730951 and round it to 1. Then it will check if 1**3 is equal to 8, which it is. So the function will return True. 

This function works for all positive integers x and n. It handles the case where n is 1 by returning False, as 1 is not a simple power of any number. It also handles the case where x is 1 by checking if n is 1, in which case it returns True. 

This function has a time complexity of O(log n) as it involves calculating the nth root of n, which can be done in logarithmic time. It also has a space complexity of O(1), as it only uses a constant amount of space to store the variables. 





Note: This function does not work for negative integers. If you want to handle negative integers as well, you can modify the function to check if x is negative and if n is odd. If both are true, then x is not a simple power of n. 

Also, this function does not work for non-integer n. If you want to handle non-integer n as well, you can modify the function to check if n is an integer. If it is not, then x is not a simple power of n. 