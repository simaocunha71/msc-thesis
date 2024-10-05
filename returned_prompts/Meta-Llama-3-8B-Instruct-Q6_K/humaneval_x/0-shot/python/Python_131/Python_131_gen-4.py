```
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2 != 0:
            product *= int(digit)
    return product
```


Explanation:
The function `digits(n)` takes a positive integer `n` as input and returns the product of its odd digits. If all digits are even, it returns 0.

The function converts the integer `n` to a string using `str(n)`, which allows it to iterate over each digit. For each digit, it checks if the digit is odd by using the modulus operator `%` with 2. If the remainder is not 0, the digit is odd and the product is updated by multiplying it with the current product.

Finally, the function returns the product of the odd digits. If no odd digits are found, the product remains 1 and the function returns 0.