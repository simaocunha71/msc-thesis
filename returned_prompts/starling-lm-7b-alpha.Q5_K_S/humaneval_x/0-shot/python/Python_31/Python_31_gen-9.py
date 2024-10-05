To determine if a number is prime, we can follow these steps:

Check if the number is less than or equal to 1. If it is, return False because prime numbers are greater than 1.
Check if the number is 2. If it is, return True because 2 is the only even prime number.
Check if the number is divisible by 2. If it is, return False because even numbers (except 2) are not prime.
Check if the number is divisible by any number in the range 3 to the square root of the number. If it is, return False because a number that can be evenly divided by another number in this range cannot be prime.
If none of the above conditions are met, return True because the number is prime.

Here's an implementation of the is_prime function in Python:

def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
In this implementation, the function takes a number n as an argument and returns True if n is prime, and False otherwise. The function first checks if n is less than or equal to 1, and if so, returns False. Then, it checks if n is equal to 2, and if so, returns True. Next, it checks if n is divisible by 2, and if so, returns False. Finally, it checks if n is divisible by any odd number in the range 3 to the square root of n, and if so, returns False. If none of these conditions are met, the function returns True, indicating that n is prime.

You can test the function with the provided test cases or with your own examples to ensure that it is working correctly.



























































