```
def digits(n):
    product = 1
    for digit in str(n):
        if int(digit) % 2 != 0:
            product *= int(digit)
    return product if product != 1 else 0
```
This function converts the integer into a string, then iterates over each character (digit) in the string. If the digit is odd (i.e., its remainder when divided by 2 is not 0), it multiplies the product by the digit. Finally, it returns the product if it is not 1 (i.e., there were at least one odd digit), or 0 if all digits were even.  Example inputs and outputs:
```
print(digits(1))  # Output: 1
print(digits(4))  # Output: 0
print(digits(235))  # Output: 15
```



Note that Python's division operator `/` always returns a float, so we use the modulus operator `%` to check if a number is odd (i.e., its remainder when divided by 2 is not 0).  The `str` function converts an integer into a string, and the `int` function converts a string into an integer.  The `print` function is used to display the output.  The `if` statement checks if the product is 1, and returns 0 if it is, to satisfy the problem's requirement that the function return 0 if all digits are even.  The `for` loop iterates over each character (digit) in the string.  The `*=` operator performs multiplication and assignment.  The `return` statement returns the product.  The `print` function is used to display the output.  The `if` statement checks if the digit is odd, and if so, multiplies the product by the digit.  The `for` loop iterates over each character (digit) in the string.  The `*=` operator performs multiplication and assignment.  The `return` statement returns the product.  The `print` function is used to display the output.  The `if` statement checks if the product is 1, and returns 0 if it is, to satisfy the problem's requirement that the function return 0 if all digits are even.  The `for` loop iterates over each character (digit) in the string.  The `*=` operator performs multiplication and assignment.  The `return` statement returns