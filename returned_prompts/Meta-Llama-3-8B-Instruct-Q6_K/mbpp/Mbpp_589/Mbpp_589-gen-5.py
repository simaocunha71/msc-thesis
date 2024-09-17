```
def perfect_squares(a, b):
    return [i for i in range(a, b+1) if round(i**0.5)**2 == i]
```


In this function, we use list comprehension to generate a list of numbers from `a` to `b`. For each number `i` in this range, we check if the square root of `i` is an integer by checking if `round(i**0.5)**2 == i`. If this condition is true, it means `i` is a perfect square, so we include it in the list. The function returns this list of perfect squares. 

The unit test `assert perfect_squares(1,30)==[1, 4, 9, 16, 25]` shows that the function should return all perfect squares between 1 and 30, which are 1, 4, 9, 16, and 25. 

Note that the `+1` in the `range` function is necessary to include `b` in the range. Without it, `b` would not be included in the range, so the function would not return any perfect squares equal to `b`. 

The `round(i**0.5)**2 == i` condition is used to check if `i` is a perfect square. This condition is true if and only if `i` is a perfect square. The `round(i**0.5)` part is used to round the square root of `i` to the nearest integer. If `i` is a perfect square, then its square root is an integer, so `round(i**0.5)` will return this integer. The `**2` part squares this integer, so we are essentially checking if the square of the integer square root of `i` is equal to `i`. If this is true, then `i` is a perfect square. 

The function returns a list of all perfect squares between `a` and `b` (inclusive). If no perfect squares are found in the range, the function returns an empty list. 

This function assumes that `a` and `b` are integers and that `a` is less than or equal to `b`. If these assumptions are not valid, the function may not work correctly. 

The time complexity of this function is O(n), where n is the difference between `b` and `a`. This is because the function iterates over a range of `