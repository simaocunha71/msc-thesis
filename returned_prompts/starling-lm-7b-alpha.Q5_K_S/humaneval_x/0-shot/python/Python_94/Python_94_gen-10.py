To solve this problem, you can follow these steps:

1. Find the maximum number in the list. This can be done using the built-in max() function in Python.
2. Check if the maximum number is prime. A prime number is a number greater than 1 that has no divisors other than 1 and itself. You can use a function like is_prime() to check if a number is prime.
3. If the maximum number is prime, find the sum of its digits. This can be done by converting the number to a string, iterating through each character, and adding the numerical value of each character to the sum.
4. Return the sum of the digits of the maximum prime number.

Here is an example implementation of the solution in Python:

```python
def skjkasdkd(lst):
    max_num = max(lst)
    if is_prime(max_num):
        return sum(int(digit) for digit in str(max_num))
    else:
        return -1
```

Note that the is_prime() function is not provided in the solution. You can implement it separately using various algorithms like trial division or the Sieve of Eratosthenes.

Make sure to handle the case where there are no prime numbers in the list by returning -1 or any appropriate value.

I hope this helps you solve the problem! Let me know if you have any further questions.

```python
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
```

This implementation of the is_prime() function checks if a number is prime by iterating through all numbers from 2 to the square root of the number (inclusive) and checking if the number is divisible by any of them. If it is divisible by any of them, it is not prime.

You can use this function in the skjkasdkd() function to determine if a number is prime or not.

I hope this helps you understand the solution better! Let me know if you have any more questions.

```python
def is_prime(