```
def count_Primes_nums(n):
    if n < 2:
        return 0
    primes = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return len(primes)
```


In this function, we start by checking if the input number `n` is less than 2. If it is, we return 0 because there are no prime numbers less than 2. Then, we initialize an empty list `primes` to store the prime numbers. We iterate over the range from 2 to `n-1` (since 0 and 1 are not prime), and for each number `i`, we check if it is prime by iterating over the range from 2 to the square root of `i` (inclusive). If `i` is not divisible by any of these numbers, we consider it prime and add it to the `primes` list. Finally, we return the length of the `primes` list, which represents the number of prime numbers less than `n`. 
The unit test `assert count_Primes_nums(5) == 2` helps to clarify the problem by providing an example of the expected output. In this case, the function should return 2 because there are two prime numbers less than 5: 2 and 3. 





The function works by checking each number in the range [2, n) to see if it's prime. A prime number is a number that is divisible only by 1 and itself. The function checks this by iterating over the range [2, sqrt(i)) and seeing if i is divisible by any of these numbers. If it is, then i is not prime, so the function moves on to the next number. If it's not divisible by any of these numbers, then it is prime, so the function adds it to the list of primes. Finally, the function returns the length of this list, which is the number of primes less than n.