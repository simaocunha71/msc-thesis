```
def cube_nums(lst):
    return [i**3 for i in lst]
```


The problem asks to create a function that takes a list of numbers as input and returns a new list where each element is the cube of the corresponding element in the input list.

The unit test provided helps to clarify the problem by showing the expected output for a given input. In this case, the input is a list of integers from 1 to 10, and the expected output is a list of their cubes.

The solution uses a list comprehension in Python, which is a concise way to create a new list by performing an operation on each element of an existing list. In this case, the operation is the cube function, which is represented by `i**3`. The result is a new list where each element is the cube of the corresponding element in the input list.