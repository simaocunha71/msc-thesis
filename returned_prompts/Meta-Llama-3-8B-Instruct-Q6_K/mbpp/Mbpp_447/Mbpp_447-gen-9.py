```
def cube_nums(lst):
    return [i**3 for i in lst]
```





Python code that defines a function `cube_nums` which takes a list of numbers as input and returns a new list where each number is replaced by its cube.

The function uses a list comprehension to iterate over the input list, cube each number using the `**` operator, and create a new list with the cubed values.

For example, if the input list is `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, the function will return the list `[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]`.

The unit test `assert cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]` ensures that the function behaves correctly by comparing its output with the expected result.