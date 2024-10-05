```
def prime_length(string):
    length = len(string)
    if length < 2:
        return True
    for i in range(2, int(length**0.5) + 1):
        if length % i == 0:
            return False
    return True
```


The function first calculates the length of the input string. If the length is less than 2, it returns True because 0 and 1 are considered prime numbers. Then it checks if the length is divisible by any number from 2 to the square root of the length. If it is, the function returns False because the length is not a prime number. If the length is not divisible by any of these numbers, the function returns True because the length is a prime number. The square root optimization is used to reduce the number of iterations in the loop. This optimization is possible because a larger factor of the number would be a multiple of smaller factor that has already been checked.  For example, if 5 is a factor of the number, 10 would have been checked before 5. Therefore, we only need to check up to the square root of the number.