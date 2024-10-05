```
def multiply(a, b):
    return (a % 10) * (b % 10)
```




Solution:
```
def multiply(a, b):
    return (a % 10) * (b % 10)
```

Explanation:
The function takes two integers as input and returns the product of their unit digits. The unit digit of a number is the remainder of the number when divided by 10. We use the modulus operator `%` to get the unit digit of each number and then multiply them together. This ensures that we only consider the last digit of each number and ignore the rest of the digits. For example, if we have the numbers 148 and 412, the function would return the product of their unit digits, which is 8 and 2, respectively, resulting in a product of 16.