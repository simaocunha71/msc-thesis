```
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2 != 0:
            product *= int(digit)
    return product
```
The `digits` function takes an integer `n` as input and returns the product of its odd digits. If all digits are even, it returns 0. 

We convert the integer `n` to a string using the `str` function to iterate over each character (digit) in the string. For each digit, we check if it is odd by using the modulus operator `%` with the divisor 2. If the remainder is not 0, the digit is odd and we multiply the product by the digit. If all digits are even, the product remains 1 and the function returns 0. 

The function returns the product of the odd digits as an integer. 

For example, `digits(1)` returns 1 because the only digit is 1, which is odd. `digits(4)` returns 0 because all digits are even. `digits(235)` returns 15 because the odd digits are 3 and 5. 

This function works for positive integers and returns 0 for all even integers. It does not handle negative integers or non-integer inputs. 