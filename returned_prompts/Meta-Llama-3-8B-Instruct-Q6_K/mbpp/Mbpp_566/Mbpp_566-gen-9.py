```
def sum_digits(n):
    return sum(int(digit) for digit in str(n))
```


Here, we convert the integer to a string, and then iterate over each character (digit) in the string. We convert each character back to an integer and sum them up. This function should pass the given unit test.