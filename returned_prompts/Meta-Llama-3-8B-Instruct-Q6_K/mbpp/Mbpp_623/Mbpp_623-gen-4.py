```
def nth_nums(lst, n):
    return [x**n for x in lst]
```



The problem is asking to write a function that takes a list of numbers and an integer `n` as input, and returns a new list where each number in the input list is raised to the power of `n`.

The unit test `assert nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2)==[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]` suggests that the function should return a list where each number in the input list is squared.

Here is the solution:
```
def nth_nums(lst, n):
    return [x**n for x in lst]
```
This function uses a list comprehension to create a new list where each element is the result of raising the corresponding element in the input list to the power of `n`. The `**` operator is used to raise a number to a power. For example, `x**2` would square the number `x`. The resulting list is then returned by the function.