```
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2 != 0:
            product *= int(digit)
    return product
```



This function takes a positive integer `n` as input, converts it to a string, and then iterates over each character (digit) in the string. For each digit, it checks if the digit is odd (i.e., if the remainder when divided by 2 is not 0). If the digit is odd, it multiplies the product by the digit. If all digits are even, the product remains 1, and the function returns 0. Otherwise, it returns the product of the odd digits.