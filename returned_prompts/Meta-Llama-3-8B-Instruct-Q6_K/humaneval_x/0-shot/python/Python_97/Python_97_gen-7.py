```
def multiply(a, b):
    return (a % 10) * (b % 10)
```





The function takes two integers as input and returns the product of their unit digits. It does this by using the modulus operator (`%`) to extract the last digit of each number, then multiplying these digits together.

For example, if `a` is 148 and `b` is 412, the function will calculate the product of the last digits of these numbers, which are 8 and 2, and return 16. If `a` is 19 and `b` is 28, the function will calculate the product of the last digits of these numbers, which are 9 and 8, and return 72. If `a` is 2020 and `b` is 1851, the function will calculate the product of the last digits of these numbers, which are 0 and 1, and return 0. If `a` is 14 and `b` is -15, the function will calculate the product of the last digits of these numbers, which are 4 and -5, and return 20.

The function assumes that the input is always valid, meaning that the input will always be integers. It does not handle any exceptions or errors.