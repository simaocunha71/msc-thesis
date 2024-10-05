
To solve this problem, we can start by finding all the factors of the number n. We can do this by using a loop to check all the numbers from 2 up to the square root of n, and then check if any of these numbers are factors of n.

Once we have found all the factors, we can then check if any of them are prime. We can do this by using another loop to check if the factor is divisible by any other number from 2 up to its square root. If it is not divisible by any of these numbers, then it is a prime number.

Finally, we can return the largest prime factor that we have found.

Here is an example implementation of the solution in Python:

```python
def largest_prime_factor(n: int):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return max(factors)
```

This code first initializes an empty list called `factors` to store all the factors of n. It then starts a loop at i = 2, and continues until i * i is greater than n. Inside the loop, it checks if n is divisible by i. If it is not, it increments i by 1. If it is, it divides n by i and adds i to the `factors` list. Once the loop is finished, it checks if n is greater than 1. If it is, it means that n itself is a factor, so it adds it to the `factors` list. Finally, it returns the maximum value in the `factors` list, which is the largest prime factor of n.

You can test this function with the given test cases:

```python
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

These test cases will return the correct largest prime factors of the given numbers.

I hope this helps! Let me know if you have any more questions.

- ChatG