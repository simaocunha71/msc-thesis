```
def min_of_three(a,b,c):
    if a<b and a<c:
        return a
    elif b<c:
        return b
    else:
        return c
```

Here's some Python code that defines a function called `min_of_three` that takes three arguments, `a`, `b`, and `c`. The function compares the values of these three numbers and returns the smallest one. The assertion in the provided code is checking if the function correctly returns 0 when given the inputs 10, 20, and 0.

The `min_of_three` function uses a series of conditional statements (`if`, `elif`, and `else`) to determine which number is the smallest among the three. It first checks if `a` is less than both `b` and `c`. If this condition is true, it means that `a` is the smallest number, so it is returned by the function. If not, it moves to the next condition and checks if `b` is less than `c`. If this condition is true, it means that `b` is the smallest number, so it is returned. If neither of these conditions are true, it means that `c` is the largest number, so it is returned.

The provided assertion is a way to verify that the `min_of_three` function is working correctly. It compares the result of calling the function with the inputs 10, 20, and 0 (`min_of_three(10,20,0)`) to the expected result of 0. If the two values are not equal, the assertion will fail, indicating that there is an error in the function. In this case, since the two values are equal, the assertion passes, confirming that the `min_of_three` function correctly returns the smallest of the three input numbers.

Overall, this code defines a function that finds the minimum of three numbers and provides a test case to verify its correctness.

```python
def min_of_three(a,b,c):
    if a<b and a<c:
        return a
    elif b<c:
        return b
    else:
        return c

assert min_of_three(1