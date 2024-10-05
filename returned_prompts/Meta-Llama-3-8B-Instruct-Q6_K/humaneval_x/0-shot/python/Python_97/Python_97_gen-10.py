```
def multiply(a, b):
    return (a % 10) * (b % 10)
```





This function takes two integers as input and returns the product of their unit digits. The unit digit of a number is the remainder when the number is divided by 10. The function uses the modulus operator `%` to find the unit digits of the input numbers, and then returns their product. For example, `multiply(148, 412)` would return `(8 % 10) * (2 % 10) = 8 * 2 = 16`.