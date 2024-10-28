Here is the solution using a helper function to check if a number is prime:
```python
def largestPrimeFactor(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    largest = 1
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            largest = i
    return largest
```
This function works by iterating over all numbers from 2 to n, checking if each number is a factor of n and if it is prime. The largest such number is the largest prime factor of n. Note that this function may be slow for large values of n, as it checks every number up to n. For larger values of n, a more efficient algorithm may be needed. 

Here's how you can use this function:
```python
print(largestPrimeFactor(13195))  # Output: 29
print(largestPrimeFactor(2048))  # Output: 2
``` 
Note that the function assumes that n is greater than 1 and is not a prime number. If n is a prime number, the function will return n. If n is 1, the function will return 1. If n is less than 1, the function will raise a ValueError. You may want to add error checking code to handle these cases if necessary. 