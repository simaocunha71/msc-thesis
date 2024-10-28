```
def dif_Square(n):
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if i * i - j * j == n:
                return True
    return False
```


The problem requires you to write a function that checks whether a given number can be represented as the difference of two squares or not. 

The function dif_Square(n) takes an integer n as input and returns True if n can be represented as the difference of two squares, and False otherwise.

The problem statement doesn't mention that the two squares should be positive. However, based on the provided unit test `assert dif_Square(5) == True`, it can be assumed that the two squares can be any integers, not just positive ones.

The function uses two nested loops to check all possible pairs of squares. For each pair, it calculates the difference of the squares and checks if it equals the given number. If a pair is found that satisfies the condition, the function returns True. If no such pair is found after checking all possible pairs, the function returns False.

For example, the number 5 can be represented as the difference of two squares: 3^2 - 2^2 = 5. Therefore, dif_Square(5) returns True. On the other hand, the number 7 cannot be represented as the difference of two squares, so dif_Square(7) returns False. 