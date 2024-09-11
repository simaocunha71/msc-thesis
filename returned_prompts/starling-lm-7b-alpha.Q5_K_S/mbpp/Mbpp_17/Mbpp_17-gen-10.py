```
def square_perimeter(side):
    return 4 * side
```

Explanation:
To calculate the perimeter of a square, you need to multiply the length of one side by 4. The function `square_perimeter` takes a single parameter, `side`, which represents the length of one side of the square. Inside the function, we multiply `side` by 4 and return the result, which gives us the perimeter of the square.

In the provided test case, `square_perimeter(10)` is called with the side length of 10. The function returns 40, which is the correct perimeter of the square with a side length of 10.

You can verify the correctness of the function by adding the `assert` statement at the end. This statement checks if the returned value of `square_perimeter(10)` is equal to 40. If the condition is true, the assertion passes and the program continues executing; if it's false, an error is raised, indicating that the function is not correctly implemented.

Overall, this function provides a straightforward way to calculate the perimeter of a square given its side length as input.

```python
def square_perimeter(side):
    return 4 * side

# Test the function
assert square_perimeter(10) == 40
```

This code snippet defines the function `square_perimeter` and tests it with the side length of 10. The `assert` statement checks if the result of `square_perimeter(10)` is equal to 40. If the condition is true, the program continues; if it's false, an error is raised.
```

```
