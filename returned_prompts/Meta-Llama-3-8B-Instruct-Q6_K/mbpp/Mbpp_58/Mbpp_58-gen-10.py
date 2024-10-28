```
def opposite_Signs(a, b):
    if a >= 0 and b < 0:
        return True
    elif a < 0 and b >= 0:
        return True
    else:
        return False
```


Explanation:
The function `opposite_Signs` takes two integers `a` and `b` as input. It checks if one of the numbers is positive and the other is negative, or vice versa. If the condition is met, it returns `True`; otherwise, it returns `False`.

The unit test `assert opposite_Signs(1,-2) == True` confirms that the function works correctly. It checks if the numbers 1 and -2 have opposite signs, which is true, and the function returns `True` as expected.

This function can be used to check if two numbers have opposite signs in various applications, such as in mathematical operations, data processing, or game development. For instance, in a game, it can be used to determine if a player's score has changed sign, indicating a reversal in direction or a new game state.