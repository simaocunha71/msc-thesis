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
        if is_prime(i):
            for j in range(i, 100):
                if is_prime(j):
                    for k in range(j, 100):
                        if is_prime(k):
                            if i * j * k == a:
                                return True
    return False
```


This function first defines a helper function `is_prime(n)` to check if a number is prime. Then it iterates over all numbers from 2 to 100, checks if each number is prime, and if it is, it iterates over all numbers from that prime number to 100, checks if each number is prime, and if it is, it iterates over all numbers from that prime number to 100, checks if each number is prime, and if it is, it checks if the product of the three prime numbers is equal to the given number. If it finds such a product, it returns `True`. If it doesn't find such a product after checking all numbers, it returns `False`. 

This solution has a time complexity of O(n^2) because it uses three nested loops to check all possible products of prime numbers. This solution may not be efficient for large numbers. 

However, since the problem states that the given number is less than 100, this solution is sufficient. 

Also, this solution does not handle the case where the given number is not a product of three prime numbers. It simply returns `False` in this case. If you want to handle this case differently, you can add additional code to return a specific value, such as `None`, or to raise an exception. 

This solution is not optimized for performance and may not work correctly for larger numbers. If you need a solution that works for larger numbers, you should consider using a more efficient algorithm, such as the Sieve of Eratosthenes to generate prime numbers. 

This solution is also not optimized for readability and maintainability. It is a simple and straightforward solution, but it is not easy to understand and modify. If you need a solution that is easy to understand and modify, you should consider breaking it down into smaller functions or using more descriptive variable names.