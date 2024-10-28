The problem is asking to find the nth star number. A star number is a number that is one less than a perfect square. For example, 9 is a star number because it is one less than 10, which is a perfect square.

The unit test `assert find_star_num(3) == 37` suggests that the nth star number is the number that is one less than the nth perfect square.

Here is a Python function that solves the problem:

```
import math

def find_star_num(n):
    square = 1
    while True:
        if (math.sqrt(square) % 1 == 0):
            if n == 1:
                return square - 1
            n -= 1
        square += 1
```

This function starts from 1 and keeps incrementing until it finds a perfect square. If the perfect square is the nth perfect square, it returns the number that is one less than the perfect square. Otherwise, it decrements the count and continues. The function stops when it finds the nth star number.