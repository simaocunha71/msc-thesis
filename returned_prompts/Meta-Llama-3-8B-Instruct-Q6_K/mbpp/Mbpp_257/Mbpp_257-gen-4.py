The problem is asking for a function that takes two numbers as input and returns a tuple with the second number followed by the first number. 

Here's how you can solve it in Python:
```
def swap_numbers(a, b):
    return (b, a)
```
This function works by directly returning a tuple with `b` as the first element and `a` as the second element. The unit test `assert swap_numbers(10,20)==(20,10)` ensures that this function works correctly. 

For example, if you call `swap_numbers(10, 20)`, it will return `(20, 10)`, which is the correct result. 

This function is simple and efficient, and it passes the given unit test. 