```
def is_perfect_square(n):
    if n < 0:
        return False
    sqrt = int(n**0.5)
    return sqrt * sqrt == n
```  # Corrected the function
```
Explanation:
The function is_perfect_square(n) checks whether the given number n is a perfect square or not. 
It first checks if n is less than 0, in which case it returns False because perfect squares are always non-negative.
Then it calculates the square root of n and converts it to an integer using the int() function.
Finally, it checks if the square of this integer is equal to n. If it is, then n is a perfect square and the function returns True; otherwise, it returns False.
```  # Corrected the explanation
```  # Corrected the comment
```

The unit test `assert not is_perfect_square(10)` is also correct. It checks that the function correctly returns False for the number 10, which is not a perfect square.