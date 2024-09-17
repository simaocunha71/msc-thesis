The problem asks to write a function that takes two numbers as input and returns a tuple with the second number first and then the first number.

The unit test `assert swap_numbers(10,20)==(20,10)` suggests that the function should swap the input numbers.

Here is the solution:
```python
def swap_numbers(a, b):
    return (b, a)
```



Note: The unit test `assert swap_numbers(10,20)==(20,10)` ensures that the function swaps the input numbers correctly. It checks if the function returns a tuple with the second number first and then the first number, which is the expected behavior.