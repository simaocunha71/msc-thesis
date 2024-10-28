```
def count_Primes_nums(n):
    if n < 2:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    p = 2
    while p * p < n:
        if primes[p]:
            for i in range(p * p, n, p):
                primes[i] = False
        p += 1
    return sum(1 for p in range(2, n) if primes[p])
```
This function uses the Sieve of Eratosthenes algorithm to find all prime numbers less than the given number. The function starts by initializing a list of boolean values, where each value represents whether a number is prime or not. It then iterates over the list, marking the multiples of each prime number as not prime. Finally, it returns the count of prime numbers by summing up the boolean values in the list. 

The unit test `assert count_Primes_nums(5) == 2` ensures that the function correctly counts the prime numbers less than 5, which are 2 and 3. 

The time complexity of this function is O(n log log n) and the space complexity is O(n).  This is because the function iterates over the list of boolean values n times, and the list has a size of n. The function also uses a loop that runs up to the square root of n, which is a logarithmic factor in the time complexity.  The space complexity is linear because the function uses a list of boolean values of size n.  The function is efficient for large inputs because the Sieve of Eratosthenes algorithm is a well-known and efficient algorithm for finding prime numbers.  However, for very large inputs, the function may still be slow because the space complexity is linear.  For such large inputs, a more efficient algorithm or data structure may be needed.  For example, a bit array could be used to reduce the space complexity to O(n / 32) for 32-bit integers.  However, this would increase the time complexity to O(n / 32 log log n) because the function would need to iterate over the bit array n / 32 times.  Therefore, the choice of data structure and algorithm depends on the specific requirements of the problem and the constraints of the input.  In general, it is important to carefully consider the time and space complexity of an algorithm and to choose the best approach for the specific