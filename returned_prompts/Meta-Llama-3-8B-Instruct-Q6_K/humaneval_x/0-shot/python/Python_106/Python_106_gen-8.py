```
def f(n):
    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            result.append(factorial(i))
        else:
            result.append(sum(range(1, i+1)))
    return result

import math
def factorial(n):
    return math.factorial(n)
```


Explanation:
The function f takes an integer n as a parameter and returns a list of size n. For each index i in the range from 1 to n, if i is even (i.e., i % 2 == 0), the function appends the factorial of i to the result list. If i is odd, it appends the sum of numbers from 1 to i to the result list. The result list is then returned.

The factorial function is a helper function that calculates the factorial of a given integer n using the math.factorial function from the math module.

Example:
f(5) returns [1, 2, 6, 24, 15], which is the expected result. The first element is 1 (the factorial of 1), the second element is 2 (the sum of numbers from 1 to 2), the third element is 6 (the factorial of 3), the fourth element is 24 (the factorial of 4), and the fifth element is 15 (the sum of numbers from 1 to 5).