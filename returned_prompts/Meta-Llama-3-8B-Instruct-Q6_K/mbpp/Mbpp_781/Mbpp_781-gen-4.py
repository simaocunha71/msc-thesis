```
def count_divisors(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count % 2 == 0
```
This function counts the number of divisors for a given number `n` and checks if the count is even. The unit test `assert count_divisors(10)` checks if the function returns `True` for the number `10`, which has an even number of divisors (1, 2, 5, 10). 

Note: This function has a time complexity of O(n), which may not be efficient for large numbers. For a more efficient solution, you can use the prime factorization of the number and count the number of prime factors, which can be done in O(sqrt(n)) time. 

Here is the more efficient version of the function:
```
def count_divisors(n):
    count = 0
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            count += 1
    if n > 1:
        count += 1
    return count % 2 == 0
```
This function counts the number of prime factors of the number `n` and checks if the count is even. The unit test `assert count_divisors(10)` still passes for this function. 