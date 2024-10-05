```
def prime_length(string):
    length = len(string)
    if length <= 1:
        return False
    for i in range(2, int(length ** 0.5) + 1):
        if length % i == 0:
            return False
    return True
```


Explanation:
The function `prime_length` takes a string as input and returns `True` if the length of the string is a prime number, and `False` otherwise.

First, it calculates the length of the string using the `len` function.

Then, it checks if the length is less than or equal to 1. If it is, it immediately returns `False` because 1 is not a prime number.

Next, it iterates over all numbers from 2 to the square root of the length (inclusive). For each number `i` in this range, it checks if the length is divisible by `i` using the modulo operator (`%`). If it is, it means that the length is not a prime number, so it returns `False`.

If the function hasn't returned `False` by now, it means that the length is a prime number, so it returns `True`.