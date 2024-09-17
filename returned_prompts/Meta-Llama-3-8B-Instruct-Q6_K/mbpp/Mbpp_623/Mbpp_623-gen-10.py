```
def nth_nums(nums, n):
    return [x**n for x in nums]
```
The problem asks you to create a function that takes a list of numbers and an integer n, and returns a new list where each number in the original list is raised to the power of n.

The unit test `assert nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2)==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]` helps to clarify the problem by showing that the function should return a list where each number is raised to the power of n.

Here is the solution using a list comprehension:
```
def nth_nums(nums, n):
    return [x**n for x in nums]
```
This function uses a list comprehension to create a new list where each element is the result of raising the corresponding element in the input list to the power of n. The `**` operator is used to raise a number to a power. For example, `2**2` would evaluate to 4. The list comprehension is a concise way to create a new list from an existing list by applying a transformation to each element. In this case, the transformation is raising each number to the power of n. The resulting list is then returned by the function.