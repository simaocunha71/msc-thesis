The task is to write a function in Python that takes a list of numbers as input and returns a new list containing only the even numbers from the original list.

The unit test `assert Split([1,2,3,4,5]) == [2,4]` suggests that the function should return a list of even numbers.

Here is the solution:
```python
def Split(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers
```
This function uses a list comprehension to iterate over the input list `numbers` and includes only the numbers that are even (i.e., `num % 2 == 0`). The resulting list of even numbers is then returned.