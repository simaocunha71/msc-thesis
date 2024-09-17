```
def prime_num(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```
This function takes an integer `n` as input and returns `True` if it is a prime number, and `False` otherwise. It first checks if `n` is less than 2, in which case it is not prime. Then it iterates from 2 to the square root of `n` (inclusive) and checks if `n` is divisible by any of these numbers. If it is, then `n` is not prime. If it is not divisible by any of these numbers, then `n` is prime. 

The unit test `assert prime_num(13) == True` ensures that the function returns `True` for the prime number 13. 

The time complexity of this function is O(sqrt(n)), where `n` is the input number. This is because we only need to check divisibility up to the square root of `n`, which is a much smaller range than checking all the way up to `n`. The space complexity is O(1), which means the space required does not change with the size of the input, because we only use a constant amount of space to store the loop variable and the result. 







