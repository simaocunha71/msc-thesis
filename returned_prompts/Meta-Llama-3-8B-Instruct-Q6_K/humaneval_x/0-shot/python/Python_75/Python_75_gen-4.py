```
def is_multiply_prime(a):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for i in range(2, 100):
        if is_prime(i) and a % i == 0:
            for j in range(i, 100):
                if is_prime(j) and a % j == 0:
                    for k in range(j, 100):
                        if is_prime(k) and a % k == 0:
                            return True
    return False
```

This function works by checking all numbers from 2 to 100 to see if they are prime and if the given number can be divided by them. If it finds a prime number that can divide the given number, it checks all numbers from that prime number to 100 to see if they are also prime and can divide the given number. If it finds a second prime number that can divide the given number, it checks all numbers from that prime number to 100 to see if they are also prime and can divide the given number. If it finds a third prime number that can divide the given number, it returns True, indicating that the given number is the multiplication of three prime numbers. If it does not find any such numbers, it returns False, indicating that the given number is not the multiplication of three prime numbers. 

This function has a time complexity of O(n^3) because it checks all numbers from 2 to 100 for primality and checks all numbers from 2 to 100 to see if they can divide the given number. This is not very efficient for large numbers. A more efficient solution would be to use a sieve to generate all prime numbers up to 100 and then check if the given number can be divided by any of these prime numbers. 

This function also has a space complexity of O(1) because it only uses a constant amount of space to store the given number and the prime numbers it finds. 

This function assumes that the given number is less than 100, as stated in the problem. If the given number can be greater than 100, the function would need to be modified to handle this. 

This function also assumes that the given number is a positive integer, as stated in the problem. If the given number can be negative or a non-integer, the function