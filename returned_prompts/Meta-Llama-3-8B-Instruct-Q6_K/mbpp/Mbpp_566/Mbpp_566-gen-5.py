```
def sum_digits(n):
    return sum(int(digit) for digit in str(n))
```




    def sum_digits(n):
        return sum(int(digit) for digit in str(n))
```



The function converts the input integer to a string, then iterates over each character (digit) in the string, converts it back to an integer, and sums them all up. This is a simple and efficient way to calculate the sum of the digits of a number. The unit test `assert sum_digits(345)==12` ensures that the function works correctly.