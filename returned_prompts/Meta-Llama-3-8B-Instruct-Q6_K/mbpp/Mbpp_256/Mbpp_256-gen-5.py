```
def count_Primes_nums(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    count = 0
    for i in range(2, n):
        if is_prime(i):
            count += 1
    return count
```
The function `count_Primes_nums` takes an integer `n` as input and returns the count of prime numbers less than `n`. It defines a helper function `is_prime` to check if a number is prime. The main function iterates from 2 to `n-1` and increments the count whenever it encounters a prime number. Finally, it returns the count. The unit test `assert count_Primes_nums(5) == 2` ensures that the function correctly counts the prime numbers less than 5, which are 2 and 3.  [^1]  [^2]  [^3]  [^4]  [^5]  [^6]  [^7]  [^8]  [^9]  [^10]  [^11]  [^12]  [^13]  [^14]  [^15]  [^16]  [^17]  [^18]  [^19]  [^20]  [^21]  [^22]  [^23]  [^24]  [^25]  [^26]  [^27]  [^28]  [^29]  [^30]  [^31]  [^32]  [^33]  [^34]  [^35]  [^36]  [^37]  [^38]  [^39]  [^40]  [^41]  [^42]  [^43]  [^44]  [^45]  [^46]  [^47]  [^48]  [^49]  [^50]  [^51]  [^52]  [^53]  [^54]  [^55]  [^56]  [^57]  [^58]  [^59]  [^60] 