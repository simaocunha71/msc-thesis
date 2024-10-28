```
def cube_nums(lst):
    return [i**3 for i in lst]
```
This function uses a list comprehension to create a new list where each element is the cube of the corresponding element in the input list.

The unit test `assert cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])==[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]` ensures that the function works correctly. It checks that the output of the function when given the input `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` is `[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]`. If the function is working correctly, this assertion should pass.