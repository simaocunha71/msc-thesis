from typing import List


def factorize(n: int) -> List[int]:
    factors = []
    divisor = 2
    while divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        else:
            divisor += 1
    return factors


print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]

This code works by repeatedly dividing the input number by the smallest possible prime number (starting from 2) until the number is completely factored out. This process is repeated until the divisor is greater than the number itself. The factors are then returned in a list.

The time complexity of this code is O(n), as it loops through each number up to n once. The space complexity is also O(n), as in the worst case scenario (when the number is a prime number) all the factors will be stored in the list.

Note that this code assumes that the input number is a positive integer greater than or equal to 2. If you want to handle negative numbers or zero, you would need to add additional error checking.

Also, this code doesn't handle the case where the input number is a composite number with more than two distinct prime factors. If you want to handle such cases, you would need to modify the code to factor out all prime factors of the number, not just the first one.

Finally, this code uses integer division (//) to divide the number, which discards the remainder and gives the quotient. This is equivalent to the floor division operator (/) in Python 3, but it's used here because integer division is more commonly used in mathematics and in programming languages that don't have a built-in floating-point type.

The code is also written in Python 3. If you want to use it in Python 2, you would need to remove the type annotations and the print statements.
Code:

```python
from typing import List


def factorize(n: int) -> List[int]:
    factors = []
    divisor = 2
    while