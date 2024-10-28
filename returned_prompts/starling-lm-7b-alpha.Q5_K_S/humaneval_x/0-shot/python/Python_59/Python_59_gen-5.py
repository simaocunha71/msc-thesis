
To solve this problem, you can start by finding all the factors of the number. Then, check if each factor is a prime number. If it is, it will be the largest prime factor. Here's a step-by-step guide on how to do it:

1. Start by finding all the factors of the number. You can do this by dividing the number by all the integers less than or equal to the square root of the number. For example, if the number is 2048, the factors are 1, 2, 4, 8, 16, 32, 64, 8192, 16384, 32768, ...

2. Once you have the list of factors, you can check if each factor is a prime number. You can do this by checking if the factor is divisible by any number other than 1 and itself. If it's not divisible by any other number, it's a prime number.

3. Once you've checked all the factors, the largest one that is a prime number will be the largest prime factor of the original number.

Here's an example implementation of this algorithm in Python:

```python
def largest_prime_factor(n: int):
    factors = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    for factor in factors:
        if all(factor % i != 0 for i in range(2, int(factor**0.5) + 1)):
            return factor
```

This implementation first finds all the factors of the number and stores them in a list. Then, it checks each factor in the list to see if it's a prime number. The first factor that is a prime number is returned as the largest prime factor of the original number.

You can test this function with the provided test cases:

```python
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))  # Output