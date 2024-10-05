Here is a Python solution using a while loop to continuously divide the number by 2 until it cannot be divided any further. Then, it starts testing odd numbers starting from 3 until sqrt(n) to find the remaining factors.

```python
from typing import List
import math

def factorize(n: int) -> List[int]:
    factors = []
    # divide by 2 until n is odd
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    # n is now odd, find odd factors up to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    return factors
```
This solution works by continuously dividing the number by 2 until it cannot be divided any further. This essentially converts all the 2's into their prime factors. Then, it continues to find and append the remaining prime factors to the list. The loop stops when the remaining number is 1 or is a prime number.

This solution also takes advantage of the fact that all composite numbers have a factor less than or equal to their square root. This is used to reduce the number of iterations needed to find all factors.

The time complexity of this solution is O(sqrt(n)) because the while loop runs up to sqrt(n) times and the for loop also runs up to sqrt(n) times. The space complexity is O(1) because no additional space is used that scales with the input size.

Here are some examples of running this function with the provided test cases:

```python
print(factorize(8))  # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```
All outputs are correct for the corresponding inputs.

Please let me know if you have any other questions or if there's anything else you want to know about this solution.
"""

# ---------------------
# SOLUTION