```
def square_nums(nums):
    return [i**2 for i in nums]
```
The problem asks you to create a function that takes a list of numbers as input and returns a new list where each number is squared.

The unit test provided helps clarify the problem by showing an example of the expected output. In this case, the input is a list of integers from 1 to 10, and the output should be a list of their squares.

The solution uses a list comprehension, which is a concise way to create a new list from an existing iterable. In this case, the iterable is the input list `nums`, and the expression `i**2` squares each number.

For example, if the input is `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, the function would return the list `[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]`.