```
def cube_nums(nums):
    return [num ** 3 for num in nums]
```


The problem asks you to write a function that takes a list of numbers as input and returns a new list where each number is replaced with its cube (i.e., the result of the number multiplied by itself three times).

The unit test provided helps to clarify the problem. It shows that the function should take a list of integers, cube each integer, and return a list of the resulting cubes. For example, if the input list is `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, the output should be `[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]`.

Here's a Python function that solves the problem:
```
def cube_nums(nums):
    return [num ** 3 for num in nums]
```
This function uses a list comprehension to create a new list where each element is the cube of the corresponding element in the input list. The `**` operator is used to raise each number to the power of 3, which is the definition of a cube. The resulting list is then returned by the function.