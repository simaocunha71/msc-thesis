```
def count_up_to(n):
    if n < 1:
        return []

    primes = []
    num = 2
    while num < n:
        if is_prime(num):
            primes.append(num)
        num += 1

    return primes

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
```
This solution defines a function `count_up_to` that takes an integer `n` as input and returns an array of the first `n` integers that are prime numbers and less than `n`. 

The function uses a helper function `is_prime` to check if a number is prime. The `is_prime` function returns `False` for numbers less than 2 and then checks if the number is divisible by any integer from 2 to the square root of the number. If the number is divisible, it returns `False`; otherwise, it returns `True`.

In the `count_up_to` function, we start from 2 and iterate until we reach `n`. For each number, we check if it is prime using the `is_prime` function. If it is, we add it to the `primes` list. Finally, we return the `primes` list.

Note that we only need to check up to the square root of `n` for divisibility, because a larger factor of the number would be a multiple of a smaller factor that has already been checked. This optimization reduces the number of iterations and makes the function more efficient. 





```
print(count_up_to(5))  # [2, 3]
print(count_up_to(11))  # [2, 3, 5, 7]
print(count_up_to(0))  # []
print(count_up_to(20))  # [2, 3, 5, 7, 11, 13, 17, 19]
print(count_up_to(1))  # []
print(count_up_to(18))  # [2, 3, 5, 7, 11, 13, 17]
```



Output:

```
[2, 3]
[2, 3, 5, 7]
[]
[2, 3, 5, 7, 11, 13, 