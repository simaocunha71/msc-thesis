```
def sum_digits(n):
    return sum(int(digit) for digit in str(n))
```
This function converts the integer into a string, then uses a generator expression to iterate over each character (digit) in the string. It converts each character back into an integer using the `int()` function, and then sums up all the digits using the `sum()` function. 

For example, if we call `sum_digits(345)`, it will first convert `345` into the string `'345'`, then iterate over each character: `'3'`, `'4'`, and `'5'`. It will convert each character back into an integer: `3`, `4`, and `5`, then sum them up: `3 + 4 + 5 = 12`. 

The unit test `assert sum_digits(345)==12` ensures that the function is working correctly. 