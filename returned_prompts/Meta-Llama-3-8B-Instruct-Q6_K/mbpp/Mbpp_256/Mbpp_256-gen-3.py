```
def count_Primes_nums(n):
    if n < 2:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n, i):
                primes[j] = False
    return sum(1 for p in primes if p)
``` 
The function `count_Primes_nums(n)` counts the number of prime numbers less than the given non-negative number `n`. It starts by initializing a list `primes` of boolean values, initially set to `True`, representing whether each number from 0 to `n-1` is prime or not. It then sets `primes[0]` and `primes[1]` to `False`, as 0 and 1 are not prime numbers. 

The function then iterates over each `i` from 2 to the square root of `n`, and for each `i`, it marks as composite (`primes[j] = False`) all the multiples of `i` in the range `[i * i, n)`. This is done to optimize the process, as a composite number must have a factor less than or equal to its square root. 

Finally, the function returns the sum of all `True` values in the `primes` list, which represents the count of prime numbers less than `n`. 
The unit test `assert count_Primes_nums(5) == 2` ensures that the function correctly counts the prime numbers less than 5, which are 2 and 3. 

The time complexity of this function is O(n log log n) due to the Sieve of Eratosthenes algorithm used to generate prime numbers. The space complexity is O(n) for storing the boolean array `primes`. 
This function is efficient for large inputs, as it only requires a single pass over the numbers from 2 to the square root of `n`, and it uses a boolean array to store the primality of each number, which reduces the time complexity. 
However, for very large inputs, the function may use a significant amount of memory to store the `primes` array. 
To optimize the function for large inputs, you could use a more memory-efficient algorithm, such as the Sieve of Atkin, which has a space complexity of O