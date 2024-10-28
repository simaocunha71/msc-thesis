The function will count the total number of divisors of a given integer. The divisors of a number are the numbers that can divide the given number without leaving a remainder.

Here is a python function that does this:

```
def divisor(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count
```

This function works by iterating over all numbers from 1 to the given number. For each number, it checks if the given number is divisible by it. If it is, it increments the count of divisors. Finally, it returns the count.

The unit test `assert divisor(15) == 4` ensures that the function correctly returns the number of divisors for the input 15, which is 4 (1, 3, 5, 15). 

This function has a time complexity of O(n), where n is the given number. For large numbers, this function may be slow. A more efficient solution would be to count the divisors up to the square root of the number, and then multiply that count by 2 (because a number can also be divided by its square root). Here is the improved function:

```
import math

def divisor(n):
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
    return count
```

This function has a time complexity of O(sqrt(n)), which is much faster for large numbers.  However, for small numbers, the original function may be faster.  The choice of which function to use depends on the size of the input numbers and the requirements of the application.  The improved function is generally more efficient, but the original function may be more readable and easier to understand.  In this case, the original function is used in the solution.  If efficiency is a concern, the improved function could be used instead.  The unit test `assert divisor(15) == 4` ensures that the function correctly returns the number of divisors for the input 15, which is 4 (1, 3, 5, 15).  This unit test can be run to verify that the function works correctly for this input.  Other unit tests could be added to verify the