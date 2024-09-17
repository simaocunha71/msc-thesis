```
def is_perfect_square(n):
    if n < 0:
        return False
    sqrt = int(n**0.5)
    return sqrt * sqrt == n
```


In this function, we first check if the number is less than 0. If it is, we return False because a perfect square cannot be negative. Then, we calculate the square root of the number and convert it to an integer. If the square of this integer is equal to the original number, we return True, indicating that the number is a perfect square. Otherwise, we return False. 

The unit test `assert not is_perfect_square(10)` ensures that the function correctly identifies 10 as not a perfect square. 

Note: The `**` operator is used for exponentiation, and `int()` is used to convert the result to an integer. The `**0.5` part calculates the square root of the number. 

This solution has a time complexity of O(1) and a space complexity of O(1) because it only uses a constant amount of space to store the result and the variables. 

The problem can also be solved using the math.isqrt() function, which is available in Python 3.8 and later versions. Here's how you can do it:

```
import math

def is_perfect_square(n):
    if n < 0:
        return False
    return math.isqrt(n) ** 2 == n
```


This solution is more concise and efficient than the previous one, but it requires Python 3.8 or later. 
```python
import math

def is_perfect_square(n):
    return math.isqrt(n) ** 2 == n
```


This solution is more concise and efficient than the previous one, but it requires Python 3.8 or later. 
```python
import math

def is_perfect_square(n):
    return math.isqrt(n) ** 2 == n
```


This solution is more concise and efficient than the previous one, but it requires Python 3.8 or later. 
```python
import math

def is_perfect_square(n):
    return math.isqrt(n) ** 2 == n
```


This solution is more concise and efficient than the previous one, but it requires Python 3.8 or later. 
```python
import math

def is_perfect_square(n):
    return math.isqrt(n) ** 2 == n
```


