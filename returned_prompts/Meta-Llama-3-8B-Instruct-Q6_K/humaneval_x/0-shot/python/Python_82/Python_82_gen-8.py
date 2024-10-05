```
def prime_length(string):
    length = len(string)
    if length < 2:
        return False
    for i in range(2, int(length ** 0.5) + 1):
        if length % i == 0:
            return False
    return True
```


This function first calculates the length of the input string. It then checks if the length is less than 2, in which case it returns False because 0 and 1 are not prime numbers. Then it iterates from 2 to the square root of the length (inclusive), checking if the length is divisible by any of the numbers in this range. If it is, it returns False because the length is not a prime number. If it is not divisible by any of these numbers, it returns True because the length is a prime number. The `int(length ** 0.5) + 1` part is used to avoid unnecessary iterations by only checking divisibility up to the square root of the length. This is because a larger factor of the number would be a multiple of a smaller factor that has already been checked.