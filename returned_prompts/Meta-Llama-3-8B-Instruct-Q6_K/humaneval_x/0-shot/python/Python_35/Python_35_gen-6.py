The task is to write a function `max_element` that takes a list of numbers as input and returns the maximum element in the list.

Here's the solution:
```python
def max_element(l: list):
    return max(l)
```
Explanation:

The built-in `max` function in Python returns the largest item in an iterable or the largest of two or more arguments. We can simply use this function to find the maximum element in the list.

The unit tests provided in the problem description demonstrate the expected behavior of the function:
```python
>>> max_element([1, 2, 3])
3
>>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
123
```
These tests show that the function correctly returns the maximum element in the list. The second test has a large list with both positive and negative numbers, and the function still returns the maximum value, which is 123.