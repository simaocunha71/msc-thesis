```
def count_Primes_nums(n):
    primes = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (primes[p] == True):
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1
    count = 0
    for p in range(2, n):
        if primes[p]:
            count += 1
    return count
```


This function works by creating a list of boolean values representing the numbers from 0 to n, and initially assuming all numbers are prime. Then it iterates through the list, marking the multiples of each prime number as not prime. Finally, it counts the number of prime numbers in the list. The unit test `assert count_Primes_nums(5) == 2` confirms that this function returns the correct count for the number 5, which has two prime numbers less than it (2 and 3). 







