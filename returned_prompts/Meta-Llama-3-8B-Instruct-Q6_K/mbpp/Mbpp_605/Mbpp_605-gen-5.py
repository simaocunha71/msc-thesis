```
def prime_num(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```
The function `prime_num(n)` checks if the given integer `n` is a prime number. It returns `True` if `n` is prime and `False` otherwise. 

The function works by checking if `n` is divisible by any integer from 2 to the square root of `n`. If `n` is divisible by any of these integers, then it is not a prime number and the function returns `False`. If `n` is not divisible by any of these integers, then it is a prime number and the function returns `True`.

The unit test `assert prime_num(13)==True` ensures that the function correctly identifies 13 as a prime number. 

The time complexity of this function is O(sqrt(n)) because it needs to iterate up to the square root of `n` to check if `n` is prime. The space complexity is O(1) because it only uses a constant amount of space to store the variables. 