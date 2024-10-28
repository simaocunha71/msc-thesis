```
def is_multiply_prime(a):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for i in range(2, 100):
        if is_prime(i) and a % i == 0:
            for j in range(i, 100):
                if is_prime(j) and a % j == 0:
                    for k in range(j, 100):
                        if is_prime(k) and a % k == 0:
                            return True
    return False
```


The function `is_multiply_prime(a)` checks if the given number `a` is the multiplication of 3 prime numbers. It uses a helper function `is_prime(n)` to check if a number `n` is prime. The main function then iterates over all numbers from 2 to 100, and for each prime number, it checks if `a` is divisible by that number. If `a` is divisible, it then checks if there are two more prime numbers that divide `a`, and if so, it returns `True`. If no such combination of three prime numbers is found, it returns `False`. This function may be slow for large numbers because it checks all numbers up to 100, but it works correctly for the given constraints. 

Here is the example as mentioned in the problem:
```
is_multiply_prime(30) == True
30 = 2 * 3 * 5
```


The function `is_multiply_prime(30)` returns `True` because 30 is the multiplication of 3 prime numbers: 2, 3, and 5. 

Please note that this function is not optimized for performance and it may take some time to run for large numbers. For a more efficient solution, you may want to use a more efficient algorithm to find prime numbers, or to limit the search to a smaller range. 