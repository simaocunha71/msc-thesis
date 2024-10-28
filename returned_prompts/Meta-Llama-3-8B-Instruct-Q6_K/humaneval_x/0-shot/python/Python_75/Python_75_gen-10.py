```
def is_multiply_prime(a):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_factors = []
    for i in range(2, a + 1):
        while a % i == 0:
            prime_factors.append(i)
            a //= i
    prime_factors.sort()
    return len(prime_factors) == 3 and all(is_prime(i) for i in prime_factors)
```    
Explanation:
This function `is_multiply_prime(a)` first checks if a number a is the multiplication of 3 prime numbers. It does this by first defining a helper function `is_prime(n)` that checks if a number n is prime. Then, it iterates over all numbers from 2 to a and checks if a is divisible by this number. If it is, it adds this number to the list of prime factors and divides a by this number. After that, it sorts the list of prime factors and checks if it has exactly 3 elements and if all these elements are prime. If so, it returns True, otherwise it returns False. 
The helper function `is_prime(n)` checks if a number n is prime by iterating over all numbers from 2 to the square root of n and checking if n is divisible by any of these numbers. If it is, it returns False, otherwise it returns True. 

For example, the function `is_multiply_prime(30)` returns True because 30 is the multiplication of 3 prime numbers: 2, 3 and 5. The function `is_multiply_prime(31)` returns False because 31 is not the multiplication of 3 prime numbers. 31 is a prime number itself.  The function `is_multiply_prime(28)` returns False because 28 is the multiplication of 2 and 14, and 14 is not a prime number. 14 is the multiplication of 2 and 7, and 7 is a prime number. But 28 is not the multiplication of 3 prime numbers.  The function `is_multiply_prime(2)` returns False because 2 is not the multiplication of 3 prime numbers. It is a prime number itself.  The function `is_multiply_prime(4)` returns False because 4 is the multiplication of 2 and 2, and 2 is a prime