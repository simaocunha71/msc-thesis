To determine if a given number is prime, we can follow these steps:

1. If the number is less than 2, it is not prime. We can return False in this case.
2. Check if the number is divisible by any prime numbers from 2 to the square root of the number (inclusive). If it is divisible by any of these prime numbers, it is not prime. We can return False in this case.
3. If none of the above conditions are met, the number is prime. We can return True in this case.

Here's an implementation of the is_prime function in Python:

```python
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
```

You can use this function to check if a number is prime. For example, to check if the number 13 is prime, you can call the function like this:

```python
print(is_prime(13))  # Output: True
```

The function will return True if the number is prime, and False otherwise.

It's worth noting that the function uses the math.sqrt function from the math module to calculate the square root of a number. This function is part of the Python standard library and can be imported using the import statement.

The function also uses a range loop to iterate over the prime numbers from 2 to the square root of the number (inclusive). The range function is used to generate a sequence of numbers, and the loop iterates over each number in the sequence.

Finally, the function returns True if none of the conditions are met and the number is determined to be prime. Otherwise, it returns False.

Overall, this implementation of the is_prime function is efficient and accurate, providing a reliable way to determine if a given number is prime or not.

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True